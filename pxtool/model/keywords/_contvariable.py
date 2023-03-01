from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _Contvariable(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, contvariable:str, lang:str = None) -> None:
        """ which variable is the content variable """
        LineValidator.is_not_None( self._keyword, contvariable)
        LineValidator.is_string( self._keyword, contvariable)
        my_value = _PxString(contvariable)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

