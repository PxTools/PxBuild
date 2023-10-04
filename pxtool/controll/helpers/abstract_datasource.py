import pyarrow.parquet as pq
import pandas as pd
from abc import ABC, abstractmethod


# Open and read the Parquet file

class AbstractDatasource(ABC):

   @abstractmethod 
   def PrintColumns(self) -> None:
      pass
    
   @abstractmethod 
   def GetTimePeriodesPandas(self, column_name:str) -> pd.Series:
       pass

   @abstractmethod    
   def GetRawPandas(self) -> pd.DataFrame:
      pass




