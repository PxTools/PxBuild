from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _KeytypeVariableLangMulti
from pxtool.model.util._line_validator import LineValidator

class _Partitioned(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = True

    def __init__(self, keyword:str) -> None:
        super().__init__(keyword)
        self.occurence_counter = 0

    def set(self, partitioned:list[str], variable:str, lang:str = None) -> None:
        """ string , int (,int) """
        LineValidator.is_not_None( self._keyword, partitioned)
        LineValidator.is_list_of_strings( self._keyword, partitioned)
        my_value = _PxStringList(partitioned)
        self.occurence_counter += 1
        my_key = _KeytypeVariableLangMulti(variable, lang, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableLangMulti) -> _PxStringList:
        return super().get_value(my_key)