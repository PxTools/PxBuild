from .abstract_dim import AbstractDim
from typing import Dict, List, Optional
from pxbuild.controll.helpers.datadata_helpers.datadatasource import Datadatasource
from pxbuild.controll.helpers.loaded_jsons import LoadedJsons


from pxbuild.controll.helpers.datadata_helpers.for_get_data import CubemathsHelper


class TimeDim(AbstractDim):
    def __init__(self, in_loaded_jsons: LoadedJsons, in_datadatasource: Datadatasource) -> None:
        meta = in_loaded_jsons.get_pxmetadata().dataset
        config = in_loaded_jsons.get_config()
        super().__init__(config.timevariable_code, meta.time_dimension.label)

        col_name = meta.time_dimension.column_name
        self._periods = in_datadatasource.get_timeperiodes(col_name)

        self._for_get_data = CubemathsHelper(col_name, self._periods)

    # for time : code == label

    def get_codes(self) -> List[str]:
        return self._periods

    def get_labels(self, language: str) -> List[str]:
        return self._periods

    def get_valuelabel(self, language: str, value_code: str) -> str:

        return value_code

    def get_cubemaths_helper(self, language: str) -> CubemathsHelper:
        return self._for_get_data

    def get_variabletype(self) -> str:
        return "T"
