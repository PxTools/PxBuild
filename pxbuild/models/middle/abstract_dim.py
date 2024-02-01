from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from pxbuild.controll.helpers.datadata_helpers.for_get_data import ForGetData


class AbstractDim(ABC):
    def __init__(self, code: str, label_by_lang: Dict[str, str]) -> None:
        self._code: str = code
        self.label_by_lang = label_by_lang

    def get_code(self) -> str:
        return self._code

    def get_label(self, language) -> str:
        return self.label_by_lang[language]

    # def getValuesSorted(self, language) -> List[Value]:
    #      return [valueitem.code for valueitem in self._sorted_valueitems[language]]

    @abstractmethod
    def get_valuelabel(self, language: str, value_code: str) -> str:
        pass

    @abstractmethod
    def get_ForGetData(self, language: str) -> ForGetData:
        pass

    @abstractmethod
    def get_variabletype(self) -> str:
        pass
