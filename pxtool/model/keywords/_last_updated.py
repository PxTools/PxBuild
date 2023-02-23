from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_content_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_LAST_UPDATED(_PXValueByKey): 

    def set(self, last_updated:str, content:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, last_updated)
        LineValidator.is_string( self._keyword, last_updated)
        my_value = _PxString(last_updated)
        my_key = _keytype_content_lang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

