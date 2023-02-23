from pxtool.model.util._px_super import _PXValueByKey, _PxStringList
from pxtool.model.util._px_keytypes import _keytype_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_HEADING(_PXValueByKey): 

    def set(self, heading:list[str], lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, heading)
        LineValidator.is_list_of_strings( self._keyword, heading)
        my_value = _PxStringList(heading)
        my_key = _keytype_lang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

