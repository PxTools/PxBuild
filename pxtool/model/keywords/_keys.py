from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Keys(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, keys:str, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, keys)
        LineValidator.is_string( self._keyword, keys)
        LineValidator.regexp_string("^(CODES|VALUES)$", self._keyword, keys)
        my_value = _PxString(keys)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableLang) -> _PxString:
        return super().get_value(my_key)