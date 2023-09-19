import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from typing import List

# Open and read the Parquet file

class ParquetDatasource:

   def __init__(self,filepath:str) -> None:
     print("Debug: Reading",filepath)
     self._parquet_file = pq.ParquetFile(filepath)


   def PrintColumns(self) -> None:
      print("Debug cols:",self._parquet_file.schema.names)
    
   def GetTimePeriodes(self, column_name:str) -> List[str]:
       #chat: Parquet files are designed for efficient columnar storage and retrieval but do not inherently support reading only distinct values

       # Read the entire column into a Pandas Series
       column_data = self._parquet_file.read(columns=[column_name]).to_pandas()[column_name]

       # Get distinct values from the column
       distinct_values = column_data.unique()
       asList=distinct_values.tolist()
       asSortedList=sorted(asList)[:4]
       return asSortedList
