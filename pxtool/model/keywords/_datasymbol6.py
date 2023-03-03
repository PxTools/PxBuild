from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _Datasymbol6(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = True


    def set(self, datasymbol6:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, datasymbol6)
        LineValidator.is_string( self._keyword, datasymbol6)
        my_value = _PxString(datasymbol6)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeLang) -> _PxString:
        return super().get_value(my_key)