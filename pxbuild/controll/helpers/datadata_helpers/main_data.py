from datetime import datetime
import time
import pandas as pd
import numpy as np
from typing import List, Dict

from ..small_static_functions import Commons 

from pxbuild.models.input.pydantic_pxmetadata import PxMetadata
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from pxbuild.models.middle.dims import Dims
from pxbuild.models.output.pxfile.px_file_model import PXFileModel

from .datadatasource import Datadatasource
from .for_get_data import ForGetData
from .data_formatter import DataFormatter


class MapData:

    def __init__(self, datadata:Datadatasource, pxmetadata:PxMetadata, config:PxbuildConfig, dims:Dims , lang:str) -> None:
        self._pxmetadata_model = pxmetadata
        self._datadata = datadata
        self._config = config



        self._for_get_data_by_varid: Dict[str, ForGetData] = dict()
        for dim in dims.getDimsInOutputOrder():
            self._for_get_data_by_varid[dim.get_label(lang)] = dim.get_ForGetData(lang)

        self._stub = dims.get_stub(lang )
        self._heading = dims.get_heading(lang )
        self._variables_in_output_order = Commons.get_variable_list(self._stub,self._heading)

    
    
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

        matrix_size = self.calculate_matrix_size()

        missing_row_symbol = self._pxmetadata_model.dataset.row_missing
        missing_cell_symbol = self._pxmetadata_model.dataset.cell_missing
        column_code_map = self.get_measurement_column_code_mapping()

        start_tidy = time.time()
        df = self._datadata.GetTidyDF(self._config.contvariable_code, column_code_map)

        end_tidy = time.time()
        time_used_tidy = end_tidy - start_tidy
        print("Time: GetTidyDF:", time_used_tidy)

        self.add_out_index(df)
        self.add_out_value(missing_cell_symbol, df)
        merged_df = self.add_missing_rows(matrix_size, missing_row_symbol, df)

        out_data = merged_df["out_value"].tolist()


        #this just need ForGetData to get length of codelist for heading. So a heading_dims would do
        formatter = DataFormatter(self._heading, self._for_get_data_by_varid)
        number_of_columns_per_line = formatter.calculate_line_break()

        out_model.data.set(out_data, number_of_columns_per_line)

        end_get_data = time.time()
        time_used_get_data = end_get_data - start_get_data
        print("Time: GetData:", time_used_get_data)

    def calculate_matrix_size(self) -> int:
        variables_in_output_order = self._variables_in_output_order
        curr_factor = 1
        for vari in reversed(variables_in_output_order):
            temp_for_get_data: ForGetData = self._for_get_data_by_varid[vari]
            temp_for_get_data.factor = curr_factor
            prev_number = temp_for_get_data._length_of_codelist
            curr_factor = curr_factor * prev_number

        array_size = curr_factor

        return array_size


    def add_missing_rows(self, matrix_size, missing_row_symbol, df):
        #sorts on index as sideeffect :-)
        matrix_df = pd.DataFrame({"out_index": range(matrix_size)})

        # Merge the two DataFrames
        merged_df = pd.merge(matrix_df, df, on="out_index", how="left")

        # Fill missing values with "MISSING"
        merged_df["out_value"].fillna(missing_row_symbol, inplace=True)
        return merged_df

    def add_out_value(self, missing_cell_symbol:str, df):
        start = time.time()

        conditions = [ df["VALUE"].notna() & (df["VALUE"] != ""),
                       df["SYMBOL"].notna() & (df["SYMBOL"] != "")]

        choices = [df["VALUE"].astype(str), df["SYMBOL"].astype(str)]

        df["out_value"] = np.select(conditions, choices, missing_cell_symbol)

        end = time.time()
        time_used = end - start
        print("Time: numpy select in:", time_used)

    def add_out_index(self, df):
        columns_to_sum = []
        for col in self._for_get_data_by_varid.values():
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
    

   

   