from model.util._px_super import _PXSingle, _PxString
from model.util._line_validator import LineValidator

class _PX_AXIS_VERSION(_PXSingle): 

    def set(self, axis_version:str) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, axis_version)
        LineValidator.is_string( self._keyword, axis_version)
        LineValidator.regexp_string(r"^\d{4}$", self._keyword, axis_version)
        my_value = _PxString(axis_version)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

