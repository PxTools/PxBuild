from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeContentLang
from pxtool.model.util._line_validator import LineValidator

class _Cfprices(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, cfprices:str, content:str=None, lang:str = None) -> None:
        """ Indicates if data is in current or fixed prices. C is used for Current and F for Fixed prices """
        LineValidator.is_not_None( self._keyword, cfprices)
        LineValidator.is_string( self._keyword, cfprices)
        LineValidator.regexp_string("^(C|F)$", self._keyword, cfprices)
        my_value = _PxString(cfprices)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeContentLang) -> _PxString:
        return super().get_value(my_key)