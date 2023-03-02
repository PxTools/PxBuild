from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeVariableLangMulti
from pxtool.model.util._line_validator import LineValidator

class _Note(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True

    def __init__(self, keyword:str) -> None:
        super().__init__(keyword)
        self.occurence_counter = 0

    def set(self, note:str, variable:str=None, lang:str = None) -> None:
        """ Applies to table if no subkey """
        LineValidator.is_not_None( self._keyword, note)
        LineValidator.is_string( self._keyword, note)
        my_value = _PxString(note)
        self.occurence_counter += 1
        my_key = _KeytypeVariableLangMulti(variable, lang, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableLangMulti) -> _PxString:
        return super().get_value(my_key)