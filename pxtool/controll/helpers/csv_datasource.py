import pandas as pd
from .abstract_datasource import AbstractDatasource

# Open and read the Csv file

class CsvDatasource(AbstractDatasource):

   def __init__(self,filepath:str) -> None:
     print("Debug: Reading csv file:", filepath)
     self._df = pd.read_csv(filepath , sep=';', dtype=str)
     self.PrintColumns()

   def PrintColumns(self) -> None:
      print("Debug cols:", self._df.columns)
    
   def GetTimePeriodesPandas(self, column_name:str) -> pd.Series:
       # Read the entire column into a Pandas Series
       # Check if the specified column exists in the DataFrame
       if column_name not in self._df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV file.")
       
       return self._df[column_name]

       
   def GetRawPandas(self) -> pd.DataFrame:
      raw_data: pd.DataFrame = self._df
      return raw_data


