from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_CREATION_DATE(_PXSingle): 

    def set(self, creation_date:str) -> None:
        """ Date in "Px  format" """
        LineValidator.is_not_None( self._keyword, creation_date)
        LineValidator.is_string( self._keyword, creation_date)
        my_value = _PxString(creation_date)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

