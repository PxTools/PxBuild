from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _UpdateFrequency(_PxSingle): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = False


    def set(self, update_frequency:str) -> None:
        """ Not in use """
        LineValidator.is_not_None( self._keyword, update_frequency)
        LineValidator.is_string( self._keyword, update_frequency)
        my_value = _PxString(update_frequency)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> _PxString:
        return super().get_value()