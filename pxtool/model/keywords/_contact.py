from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_content_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_CONTACT(_PXValueByKey): 

    def set(self, contact:str, content:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, contact)
        LineValidator.is_string( self._keyword, contact)
        my_value = _PxString(contact)
        my_key = _keytype_content_lang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

