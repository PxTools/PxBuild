from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_COPYRIGHT(_PXSingle): 

    def set(self, copyright:str) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, copyright)
        LineValidator.is_string( self._keyword, copyright)
        my_value = _PxString(copyright)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

