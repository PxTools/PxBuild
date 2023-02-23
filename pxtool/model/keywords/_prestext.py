from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_PRESTEXT(_PXValueByKey): 

    def set(self, prestext:int, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, prestext)
        LineValidator.is_int( self._keyword, prestext)
        LineValidator.in_range(0,3, self._keyword, prestext)
        my_value = int(prestext)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

