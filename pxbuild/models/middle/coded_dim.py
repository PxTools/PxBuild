from typing import Dict, List
from .abstract_dim import AbstractDim
from ..input.pydantic_pxmetadata import CodedDimension
from ..input.pydantic_pxcodes import Grouping

from pxbuild.controll.helpers.loaded_jsons import LoadedJsons
from pxbuild.controll.helpers.datadata_helpers.for_get_data import ForGetData
from pxbuild.models.input.helper_pxcodes import HelperPxCodes

class CodedDim(AbstractDim):
       
    def __init__(self, inCD:CodedDimension, inHelperPxCodes:HelperPxCodes , inLoadedJsons:LoadedJsons) -> None:
        meta = inLoadedJsons.get_pxmetadata().dataset
        config = inLoadedJsons.get_config()
                        
        n_code = inCD.code if inCD.code is not None else inCD.column_name
        super().__init__(n_code, inCD.label)
        self._raw = inCD
        self._pxcodes_helper = inHelperPxCodes

        self._variabletype = "G" if inCD.is_geo_variable_type else "N"

        self._column_name = inCD.column_name

    def get_pydantic(self) -> CodedDimension:
        return self._raw

    def get_codes(self, language:str) -> List[str]:
        return self._pxcodes_helper.getCodes(language)
    
    def get_labels(self,language:str) -> List[str]:
        return self._pxcodes_helper.getLabels(language)

    def get_valuelabel(self, language:str, value_code:str) -> str:
       return self._pxcodes_helper.get_label(language ,value_code)
    
    def get_ForGetData(self, language:str) -> ForGetData:      
        return  ForGetData(self._column_name, self._pxcodes_helper.getCodes(language))

    def groupings(self) -> List[Grouping]|None:
        return self._pxcodes_helper.groupings()
    
    def elimination_possible(self) -> bool:
        return self._pxcodes_helper.elimination_possible
    
    def getValueNotes(self):
        return self._pxcodes_helper.getNotes()
    
    def getEliminationLabel(self, language:str) -> str:
        return self._pxcodes_helper.getEliminationLabel(language)

    def get_variabletype(self) -> str:
        return self._variabletype
    

