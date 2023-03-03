from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeContentLang
from pxtool.model.util._line_validator import LineValidator

class _LastUpdated(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = True


    def set(self, last_updated:str, content:str=None, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, last_updated)
        LineValidator.is_string( self._keyword, last_updated)
        my_value = _PxString(last_updated)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeContentLang) -> _PxString:
        return super().get_value(my_key)