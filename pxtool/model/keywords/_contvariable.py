from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _keytype_lang
from pxtool.model.util._line_validator import LineValidator

class Contvariable(_PXValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, contvariable:str, lang:str = None) -> None:
        """ which variable is the content variable """
        LineValidator.is_not_None( self._keyword, contvariable)
        LineValidator.is_string( self._keyword, contvariable)
        my_value = _PxString(contvariable)
        my_key = _keytype_lang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

