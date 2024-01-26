from .abstract_dim import AbstractDim
from typing import Dict, List, Optional
from pxbuild.controll.helpers.datadata_helpers.datadatasource import Datadatasource
from pxbuild.controll.helpers.loaded_jsons import LoadedJsons


from pxbuild.controll.helpers.datadata_helpers.for_get_data import ForGetData

class TimeDim(AbstractDim):
       
    def __init__(self, inLoadedJsons:LoadedJsons, inDatadatasource:Datadatasource) -> None:
        meta = inLoadedJsons.get_pxmetadata().dataset
        config = inLoadedJsons.get_config()
        super().__init__(config.timevariable_code, meta.time_dimension.label)

               
        col_name = meta.time_dimension.column_name
        self._periods = inDatadatasource.GetTimePeriodes(col_name)

        self._for_get_data = ForGetData(col_name, self._periods) 


    # for time : code == label
    
    def get_codes(self) -> List[str]:
        return self._periods

    def get_labels(self,language:str) -> List[str]:
        return self._periods

    def get_valuelabel(self,language:str,value_code:str) -> str:
        
        return value_code
    
    def get_ForGetData(self,language:str) -> ForGetData:
        return self._for_get_data

    def get_variabletype(self) -> str:
        return "T"
    

