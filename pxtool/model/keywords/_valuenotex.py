from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_variable_value_lang_multi
from pxtool.model.util._line_validator import LineValidator

class _PX_VALUENOTEX(_PXValueByKey): 
    def __init__(self, keyword:str) -> None:
        super().__init__(keyword)
        self.occurence_counter = 0

    def set(self, valuenotex:str, variable:str, value:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, valuenotex)
        LineValidator.is_string( self._keyword, valuenotex)
        my_value = _PxString(valuenotex)
        self.occurence_counter += 1
        my_key = _keytype_variable_value_lang_multi(variable, value, lang, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

