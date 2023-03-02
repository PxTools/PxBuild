from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._px_keytypes import _KeytypeVariableValueLang
from pxtool.model.util._line_validator import LineValidator

class _Precision(_PxValueByKey): 

    pxvalue_type:str = "_PxInt"
    is_language_dependent:bool = True


    def set(self, precision:int, variable:str, value:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, precision)
        LineValidator.is_int( self._keyword, precision)
        my_value = _PxInt(precision)
        my_key = _KeytypeVariableValueLang(variable, value, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableValueLang) -> _PxInt:
        return super().get_value(my_key)