import pandas as pd
from abc import ABC, abstractmethod


# Open and read the Parquet file


class AbstractDatasource(ABC):
    @abstractmethod
    def get_raw_pandas(self) -> pd.DataFrame:
        pass
