import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from typing import List
from pxbuild.models.input.pydantic_pxbuildconfig import PxbuildConfig
from .parquet_datasource import ParquetDatasource
from .csv_datasource import CsvDatasource
from .abstract_datasource import AbstractDatasource

# Open and read the Parquet file  (or csv for small tests)

class Datadatasource:

   def __init__(self,file_id:str, config:PxbuildConfig) -> None:
     data_file_path_format= config.admin.px_data_resource.adress_format
     data_file_path=data_file_path_format.format(id=file_id)
     if data_file_path.endswith(".parquet"): 
          self._my_datasource:AbstractDatasource = ParquetDatasource(data_file_path)
     elif data_file_path.endswith(".csv"): 
          self._my_datasource:AbstractDatasource = CsvDatasource(data_file_path)
     else:
         raise Exception("Sorry, not implemented yet. Files must end with .parquet")
     
     self.PrintColumns()



   def PrintColumns(self) -> None:
      self._my_datasource.PrintColumns()
    
   def GetTimePeriodes(self, column_name:str) -> List[str]:
       """Reads all values from a column, applies unique and sorts descending."""
       #chat: Parquet files are designed for efficient columnar storage and retrieval but do not inherently support reading only distinct values

       # Read the entire column into a Pandas Series
       column_data = self._my_datasource.GetTimePeriodesPandas(column_name)
       # Get distinct values from the column
       distinct_values = column_data.unique()
       asList=distinct_values.tolist()
       asSortedList=sorted(asList, reverse=True)
       return asSortedList

   def GetIdentifierColumns(self, all_columns:list, measurement_map:dict) -> List[str]:
      identifier_columns = []
      for column in all_columns:
         if not (column in measurement_map.keys()):
            identifier_columns.append(column)

      return identifier_columns
   
   def AddMissingSymbolColumns(self, measurement_codes:list[str], df:pd.DataFrame):
      for code in measurement_codes:   
         if not (f"SYMBOL_{code}" in df):
            df[f"SYMBOL_{code}"] = ''
   
   def AddValuePrefix(self, measures_code_dict:dict) -> dict:
      columns_with_value = {}
      for key in measures_code_dict:
         columns_with_value[key] = f"VALUE_{measures_code_dict[key]}"

      return columns_with_value

   def GetTidyDF(self, measure_dim_name:str, column_code_map:dict) -> pd.DataFrame:

      raw_data: pd.DataFrame = self._my_datasource.GetRawPandas()
      print("raw_data.columns:",raw_data.columns)
      for col in raw_data.columns:
          if "SYMBOL" in col:
              raise Exception("Sorry, not implemented yet. Cant have SYMBOL in colname")

      measurement_codes = list(column_code_map.values())
      column_with_value_prefix = self.AddValuePrefix(column_code_map)
      identifier_columns = self.GetIdentifierColumns(raw_data.columns.values.tolist(), column_with_value_prefix)
      print("Renaming:",column_with_value_prefix) 
      raw_data.rename(columns=column_with_value_prefix, inplace=True) 
      print("Post renaming:", raw_data.columns)   
      self.AddMissingSymbolColumns(measurement_codes, raw_data)
      print("Cols before wide_to_long:",raw_data.columns)
      tidy_df = pd.wide_to_long(raw_data, stubnames=['VALUE', 'SYMBOL'], i=identifier_columns, j=measure_dim_name, sep='_', suffix=f"(!?{'|'.join(measurement_codes)})")
      tidy_df.reset_index(inplace=True)
      print("Cols after wide_to_long:", tidy_df.columns)
      

      return tidy_df




