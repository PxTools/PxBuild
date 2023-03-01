from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeContentLang
from pxtool.model.util._line_validator import LineValidator

class _Stockfa(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, stockfa:str, content:str=None, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, stockfa)
        LineValidator.is_string( self._keyword, stockfa)
        LineValidator.regexp_string("^(S|F|A)$", self._keyword, stockfa)
        my_value = _PxString(stockfa)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

