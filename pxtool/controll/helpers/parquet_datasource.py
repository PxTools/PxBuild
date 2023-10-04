import pyarrow.parquet as pq
import pandas as pd
from .abstract_datasource import AbstractDatasource

# Open and read the Parquet file

class ParquetDatasource(AbstractDatasource):

   def __init__(self,filepath:str) -> None:
     print("Debug: Reading parquet file:", filepath)
     self._parquet_file = pq.ParquetFile(filepath)
     self.PrintColumns()

   def PrintColumns(self) -> None:
      print("Debug cols:",self._parquet_file.schema.names)
    
   def GetTimePeriodesPandas(self, column_name:str) -> pd.Series:
       #chat: Parquet files are designed for efficient columnar storage and retrieval but do not inherently support reading only distinct values
       # Read the entire column into a Pandas Series
       return self._parquet_file.read(columns=[column_name]).to_pandas()[column_name]

       
   def GetRawPandas(self) -> pd.DataFrame:
      raw_data: pd.DataFrame = self._parquet_file.read().to_pandas()
      return raw_data




