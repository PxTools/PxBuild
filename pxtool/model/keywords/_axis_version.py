from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _AxisVersion(_PxSingle): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = False


    def set(self, axis_version:str) -> None:
        """ Not in use. Version number for PC-Axis  """
        LineValidator.is_not_None( self._keyword, axis_version)
        LineValidator.is_string( self._keyword, axis_version)
        LineValidator.regexp_string(r"^\d{4}$", self._keyword, axis_version)
        my_value = _PxString(axis_version)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> _PxString:
        return super().get_value()

