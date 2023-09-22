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
       asSortedList=sorted(asList)
       return asSortedList
   
   def GetTidyDF(self, measure_dim_name:str) -> pd.DataFrame:
      print("Debug cols:",self._parquet_file.schema.names)
      raw_data = self._parquet_file.read().to_pandas()
      print("raw_data",raw_data)
      #if laks
      raw_data.rename(columns={'VEKT': 'VALUE_Vekt', 'KILOPRIS': 'VALUE_Kilopris'}, inplace=True)
      raw_data['SYMBOL_Vekt'] = ''
      raw_data['SYMBOL_Kilopris'] = ''

      # end if
    
      ok_df = pd.wide_to_long(raw_data, stubnames=['VALUE', 'SYMBOL'], i=['VAREGRUPPER2', 'TID'], j=measure_dim_name, sep='_', suffix='(!?Vekt|Kilopris)')
      ok_df.reset_index(inplace=True)



      #melted_df = pd.melt(raw_data, id_vars=['VAREGRUPPER2', 'TID'], value_vars=['VEKT', 'KILOPRIS'], var_name='n', value_name='value')

      return ok_df




