from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_DATASYMBOL1(_PXValueByKey): 

    def set(self, datasymbol1:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, datasymbol1)
        LineValidator.is_string( self._keyword, datasymbol1)
        my_value = _PxString(datasymbol1)
        my_key = _keytype_lang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

