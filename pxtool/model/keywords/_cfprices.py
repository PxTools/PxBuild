from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _keytype_content_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_CFPRICES(_PXValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, cfprices:str, content:str, lang:str = None) -> None:
        """ Indicates if data is in current or fixed prices. C is used for Current and F for Fixed prices """
        LineValidator.is_not_None( self._keyword, cfprices)
        LineValidator.is_string( self._keyword, cfprices)
        LineValidator.regexp_string("^(C|F)$", self._keyword, cfprices)
        my_value = _PxString(cfprices)
        my_key = _keytype_content_lang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

