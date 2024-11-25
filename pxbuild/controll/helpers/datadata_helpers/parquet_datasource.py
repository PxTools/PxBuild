import pyarrow.parquet as pq
import pandas as pd
from .abstract_datasource import AbstractDatasource
from ...helpers.logger_config import logger

# Open and read the Parquet file


class ParquetDatasource(AbstractDatasource):
    def __init__(self, filepath: str) -> None:
        self._filepath = filepath
        logger.debug(f"Reading parquet file: {filepath}")
        self._parquet_file = pq.ParquetFile(filepath)

    def get_raw_pandas(self) -> pd.DataFrame:
        raw_data: pd.DataFrame = self._parquet_file.read().to_pandas()
        return raw_data
