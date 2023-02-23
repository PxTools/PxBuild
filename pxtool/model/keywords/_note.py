from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_variable_lang_multi
from pxtool.model.util._line_validator import LineValidator

class _PX_NOTE(_PXValueByKey): 
    def __init__(self, keyword:str) -> None:
        super().__init__(keyword)
        self.occurence_counter = 0

    def set(self, note:str, variable:str, lang:str = None) -> None:
        """ Applies to table if no subkey """
        LineValidator.is_not_None( self._keyword, note)
        LineValidator.is_string( self._keyword, note)
        my_value = _PxString(note)
        self.occurence_counter += 1
        my_key = _keytype_variable_lang_multi(variable, lang, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

