from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _NextUpdate(_PxSingle): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = False


    def set(self, next_update:str) -> None:
        """ Date in "Px  format" """
        LineValidator.is_not_None( self._keyword, next_update)
        LineValidator.is_string( self._keyword, next_update)
        my_value = _PxString(next_update)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> _PxString:
        return super().get_value()