from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_NEXT_UPDATE(_PXSingle): 

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

