from typing import List
from .abstract_dim import AbstractDim
from ..input.pydantic_pxmetadata import CodedDimension
from ..input.pydantic_pxcodes import Grouping

from pxbuild.controll.helpers.loaded_jsons import LoadedJsons
from pxbuild.controll.helpers.datadata_helpers.for_get_data import CubemathsHelper
from pxbuild.models.input.helper_pxcodes import HelperPxCodes


class CodedDim(AbstractDim):
    def __init__(self, in_cd: CodedDimension, in_helper_pxcodes: HelperPxCodes, in_loaded_jsons: LoadedJsons) -> None:
        # meta = in_loaded_jsons.get_pxmetadata().dataset
        # config = in_loaded_jsons.get_config()

        n_code = in_cd.code if in_cd.code is not None else in_cd.column_name
        super().__init__(n_code, in_cd.label)
        self._raw = in_cd

        self._pxcodes_helper = in_helper_pxcodes

        self._variabletype = "G" if in_cd.is_geo_variable_type else "N"

        self._column_name = in_cd.column_name

    def get_pydantic(self) -> CodedDimension:
        return self._raw

    def get_codes(self, language: str) -> List[str]:
        return self._pxcodes_helper.get_codes(language)

    def get_labels(self, language: str) -> List[str]:
        return self._pxcodes_helper.get_labels(language)

    def get_valuelabel(self, language: str, value_code: str) -> str:
        return self._pxcodes_helper.get_label(language, value_code)

    def get_cubemaths_helper(self, language: str) -> CubemathsHelper:
        return CubemathsHelper(self._column_name, self._pxcodes_helper.get_codes(language))

    def groupings(self) -> List[Grouping] | None:
        return self._pxcodes_helper.groupings()

    def elimination_possible(self) -> bool:
        return self._pxcodes_helper.elimination_possible

    def get_valuenotes(self):
        return self._pxcodes_helper.get_valueotes()

    def get_elimination_label(self, language: str) -> str:
        return self._pxcodes_helper.get_elimination_label(language)

    def get_variabletype(self) -> str:
        return self._variabletype

    def get_domain_id(self, language: str) -> str:
        return self._raw.codelist_id + "_" + language

    # For Support_files.py:
    def get_helper_pxcodes(self) -> HelperPxCodes:
        return self._pxcodes_helper
