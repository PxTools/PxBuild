from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_content_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_BASEPERIOD(_PXValueByKey): 

    pxvalue_type:str = _PxString
    is_language_dependent:bool = True


    def set(self, baseperiod:str, content:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, baseperiod)
        LineValidator.is_string( self._keyword, baseperiod)
        my_value = _PxString(baseperiod)
        my_key = _keytype_content_lang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

