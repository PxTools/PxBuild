import time
import pandas as pd
import numpy as np
from typing import Dict

from pxbuild.models.input.pydantic_pxmetadata import PxMetadata
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.middle.dims import Dims
from pxbuild.models.output.pxfile.px_file_model import PXFileModel

from .datadatasource import Datadatasource
from .for_get_data import CubemathsHelper
from .data_formatter import DataFormatter
from ...helpers.logger_config import logger


class MapData:
    def __init__(
        self, datadata: Datadatasource, pxmetadata: PxMetadata, config: PxbuildConfig, dims: Dims, lang: str
    ) -> None:
        self._pxmetadata_model = pxmetadata
        self._datadata = datadata
        self._config = config
        self._dims = dims
        self._lang = lang

        self._cubemaths_helper_by_codeid: Dict[str, CubemathsHelper] = dict()
        # The CubemathsHelpers is initalized in  init_cubemaths_helpers_and_calculate_matrix_size()

    def map_data(self, out_model: PXFileModel) -> None:
        # /// MINDEX:
        # /// We need to convert a point(one value for each variable) in
        # /// the cube to a number(the index of the array).
        # ///
        # /// k,j, i... 1-based counters
        # /// Nx number of values for x
        # /// Factor_k=Nj*Ni
        # /// Factor_j= Ni
        # /// Factor_i = 1
        # /// index = Factor_k*(k-1) + Factor_j*(j-1) + Factor_i(i-1) </remarks>
        #  in python things are zero-based but the idea is the same
        # /// </summary>
        if out_model.data.has_value():
            return

        start_get_data = time.time()

        matrix_size = self.init_cubemaths_helpers_and_calculate_matrix_size()

        missing_row_symbol = self._pxmetadata_model.dataset.row_missing
        missing_cell_symbol = self._pxmetadata_model.dataset.cell_missing
        column_code_map = self.get_measurement_column_code_mapping()

        start_tidy = time.time()
        df = self._datadata.get_tidy_df(self._config.contvariable_code, column_code_map)

        end_tidy = time.time()
        time_used_tidy = end_tidy - start_tidy
        logger.debug(f"Time: GetTidyDF: {time_used_tidy}")

        self.add_out_index(df)
        self.add_out_value(missing_cell_symbol, df)
        merged_df = self.add_missing_rows(matrix_size, missing_row_symbol, df)

        out_data = merged_df["out_value"].tolist()

        formatter = DataFormatter(self._dims.get_headingcodes(), self._cubemaths_helper_by_codeid)
        number_of_columns_per_line = formatter.calculate_line_break()

        out_model.data.set(out_data, number_of_columns_per_line)

        end_get_data = time.time()
        time_used_get_data = end_get_data - start_get_data
        logger.debug(f"Time: GetData: {time_used_get_data}")

    def init_cubemaths_helpers_and_calculate_matrix_size(self) -> int:

        dims_in_output_order = self._dims.get_dimcodes_in_output_order()
        curr_factor = 1
        for vari_c in reversed(dims_in_output_order):

            temp_for_get_data: CubemathsHelper = self._dims.dim_by_code[vari_c].get_cubemaths_helper(self._lang)
            temp_for_get_data.factor = curr_factor
            self._cubemaths_helper_by_codeid[vari_c] = temp_for_get_data

            prev_number = temp_for_get_data._length_of_codelist
            curr_factor = curr_factor * prev_number

        array_size = curr_factor

        return array_size

    def add_missing_rows(self, matrix_size, missing_row_symbol, df):
        # sorts on index as sideeffect :-)
        matrix_df = pd.DataFrame({"out_index": range(matrix_size)})

        # Merge the two DataFrames
        merged_df = pd.merge(matrix_df, df, on="out_index", how="left")

        # Fill missing values with "MISSING"
        merged_df["out_value"] = merged_df["out_value"].fillna(missing_row_symbol)

        return merged_df

    def add_out_value(self, missing_cell_symbol: str, df):
        start = time.time()

        conditions = [df["VALUE"].notna() & (df["VALUE"] != ""), df["SYMBOL"].notna() & (df["SYMBOL"] != "")]

        choices = [df["VALUE"].astype(str), df["SYMBOL"].astype(str)]

        df["out_value"] = np.select(conditions, choices, missing_cell_symbol)

        end = time.time()
        time_used = end - start
        logger.debug(f"Time: numpy select in: {time_used}")

    def add_out_index(self, df):
        columns_to_sum = []
        for col in self._cubemaths_helper_by_codeid.values():
            # Mapping the values using the dictionary
            contrib_col_name = "int_" + col._colname_in_dataframe
            df[contrib_col_name] = df[col._colname_in_dataframe].map(col._position_of_value) * col.factor
            columns_to_sum.append(contrib_col_name)
        df["out_index"] = df[columns_to_sum].sum(axis=1)

    def get_measurement_column_code_mapping(self) -> dict:
        column_code_map = {}
        for measurement_var in self._pxmetadata_model.dataset.measurements:
            column_code_map[measurement_var.column_name] = measurement_var.code

        return column_code_map
