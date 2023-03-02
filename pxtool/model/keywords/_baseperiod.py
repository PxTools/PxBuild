from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeContentLang
from pxtool.model.util._line_validator import LineValidator

class _Baseperiod(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, baseperiod:str, content:str=None, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, baseperiod)
        LineValidator.is_string( self._keyword, baseperiod)
        my_value = _PxString(baseperiod)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeContentLang) -> _PxString:
        return super().get_value(my_key)