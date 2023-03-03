from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeVariableValue
from pxtool.model.util._line_validator import LineValidator

class _MetaId(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = False


    def set(self, meta_id:str, variable:str=None, value:str=None) -> None:
        """ The META-ID keyword is used to reference a external meta information about a table, variable or value. Requires a separate file to resolve to urls """
        LineValidator.is_not_None( self._keyword, meta_id)
        LineValidator.is_string( self._keyword, meta_id)
        my_value = _PxString(meta_id)
        my_key = _KeytypeVariableValue(variable, value)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableValue) -> _PxString:
        return super().get_value(my_key)

