import pandas as pd
from typing import List
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from .parquet_datasource import ParquetDatasource
from .csv_datasource import CsvDatasource
from .abstract_datasource import AbstractDatasource
from ...helpers.logger_config import logger

# Open and read the Parquet file  (or csv for small tests)


class PxDataSourceError(Exception):
    """Custom exception for errors related to datasource."""

    pass


class Datadatasource:
    def __init__(self, file_id: str, config: PxbuildConfig) -> None:
        data_file_path_format = config.admin.px_data_resource.adress_format
        self._data_file_path = data_file_path_format.format(id=file_id)
        if self._data_file_path.endswith(".parquet"):
            self._my_datasource: AbstractDatasource = ParquetDatasource(self._data_file_path)
        elif self._data_file_path.endswith(".csv"):
            self._my_datasource: AbstractDatasource = CsvDatasource(self._data_file_path)
        else:
            raise NotImplementedError("Sorry, not implemented yet. Files must end with .parquet or .csv")

        self._raw_df = self._my_datasource.get_raw_pandas()

        self._validate_pandas()

    def _validate_pandas(self) -> None:
        valid_symbol_entries = ["", ".", "..", "...", "....", ".....", "......", "-"]
        err_mess_ending = " From datafile " + self._data_file_path
        my_colnames: List[str] = self._raw_df.columns.to_list()

        for col in my_colnames:
            if "." in col:
                raise PxDataSourceError(
                    "Column: "
                    + col
                    + " has a dot, if it is not so in the datafile, there probably is a duplicate in columnname. "
                    + err_mess_ending
                )
            # if not col.isupper():
            #   raise Exception("Column: " + col + " is not  UPPERCASE. "+ err_mess_ending )
            if col.endswith("_SYMBOL"):
                col_without_symbol = col[:-7]
                if col_without_symbol not in my_colnames:
                    raise PxDataSourceError(
                        "Found " + col + " ,but no matching " + col_without_symbol + " . " + err_mess_ending
                    )

                # Create a mask for invalid entries (not in valid_symbol_entries and not NaN)
                mask = ~self._raw_df[col].isin(valid_symbol_entries) & self._raw_df[col].notna()

                # Filter the DataFrame with the mask
                invalid_rows = self._raw_df[mask]
                if not invalid_rows.empty:
                    err_mess = "There are rows with bad value in " + col + " column. " + err_mess_ending
                    print(invalid_rows.head(10))
                    raise PxDataSourceError(err_mess)

    def get_timeperiodes(self, column_name: str) -> List[str]:
        """Reads all values from a column, applies unique and sorts descending."""

        if column_name not in self._raw_df.columns:
            raise PxDataSourceError(f"Column '{column_name}' not found in the CSV file.")

        column_data = self._raw_df[column_name]

        # Get distinct values from the column
        distinct_values = column_data.unique()
        as_list = distinct_values.tolist()
        as_sorted_list = sorted(as_list)
        return as_sorted_list

    def get_identifiercolumns(self, all_columns: list, measurement_map: dict) -> List[str]:
        identifier_columns = []
        for column in all_columns:
            if not (column in measurement_map.keys()):
                identifier_columns.append(column)

        return identifier_columns

    def add_missing_symbolcolumns(self, measurement_codes: list[str], df: pd.DataFrame):
        for code in measurement_codes:
            if not (f"SYMBOL_{code}" in df):
                df[f"SYMBOL_{code}"] = ""

    def make_renamedict(self, measurement_code_by_column_name: dict, columns_in_datafile) -> dict:
        my_out = {}
        for column_name in measurement_code_by_column_name:
            my_out[column_name] = f"VALUE_{measurement_code_by_column_name[column_name]}"
            corresponding_symbol_column = column_name + "_SYMBOL"
            if corresponding_symbol_column in columns_in_datafile:
                my_out[corresponding_symbol_column] = f"SYMBOL_{measurement_code_by_column_name[column_name]}"

        return my_out

    def get_tidy_df(self, measure_dim_name: str, measurement_code_by_column_name: dict) -> pd.DataFrame:
        # measure_dim_name is contvariable_code from config
        # column_code_map is
        #        for measurement_var in self._pxmetadata_model.dataset.measurements:
        #           column_code_map[measurement_var.column_name] = measurement_var.code
        # aka measurement_codeBycolumn_name

        #  CODED_DIM1;CODED_DIM2;CODED_DIM3;TIME;MEASURE1;MEASURE2;MEASURE1_SYMBOL
        # using measurement_codeBycolumn_name
        #  rename all column_name to VALUE_{code}
        #  rename all {colname}_SYMBOL -> SYMBOL_{code}
        #  add missing SYMBOL_{code}
        #  it is when we do pd.wide_to_long, this strange mix of column names and code is needed: The code in the cell is the columnnane minus "VALUE"

        raw_data: pd.DataFrame = self._my_datasource.get_raw_pandas()
        logger.debug(f"raw_data.columns: {raw_data.columns}")

        measurement_codes = list(measurement_code_by_column_name.values())
        column_with_value_prefix = self.make_renamedict(measurement_code_by_column_name, raw_data.columns)

        # todo attributes columns should not be counted as identifier_columns
        identifier_columns = self.get_identifiercolumns(raw_data.columns.values.tolist(), column_with_value_prefix)
        logger.debug(f"Renaming: {column_with_value_prefix}")
        raw_data.rename(columns=column_with_value_prefix, inplace=True)
        logger.debug(f"Post renaming: {raw_data.columns}")
        self.add_missing_symbolcolumns(measurement_codes, raw_data)
        logger.debug(f"Cols before wide_to_long: {raw_data.columns}")
        tidy_df = pd.wide_to_long(
            raw_data,
            stubnames=["VALUE", "SYMBOL"],
            i=identifier_columns,
            j=measure_dim_name,
            sep="_",
            suffix=f"(!?{'|'.join(measurement_codes)})",
        )
        tidy_df.reset_index(inplace=True)

        logger.debug(f"Cols after wide_to_long: {tidy_df.columns}")

        return tidy_df
