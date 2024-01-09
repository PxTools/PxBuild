from pxbuild.models.output.pxfile.util._px_super import _PxSingle
from pxbuild.models.output.pxfile.util._px_valuetype import _PxInt
from pxbuild.models.output.pxfile.util._line_validator import LineValidator

class _Rounding(_PxSingle): 

    pxvalue_type:str = "_PxInt"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("ROUNDING")

    def set(self, rounding:int) -> None:
        """ Not in normal use """
        LineValidator.is_not_None( self._keyword, rounding)
        LineValidator.is_int( self._keyword, rounding)
        LineValidator.in_range(0,1, self._keyword, rounding)
        my_value = _PxInt(rounding)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> int:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

