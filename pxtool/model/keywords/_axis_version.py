from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class AxisVersion(_PXSingle): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = False


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

