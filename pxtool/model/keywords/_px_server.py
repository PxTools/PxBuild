from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_PX_SERVER(_PXSingle): 

    def set(self, px_server:str) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, px_server)
        LineValidator.is_string( self._keyword, px_server)
        my_value = _PxString(px_server)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

