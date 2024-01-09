from pxbuild.models.output.pxfile.util._px_super import _PxSingle
from pxbuild.models.output.pxfile.util._px_valuetype import _PxInt
from pxbuild.models.output.pxfile.util._line_validator import LineValidator

class _Decimals(_PxSingle): 

    pxvalue_type:str = "_PxInt"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("DECIMALS")

    def set(self, decimals:int) -> None:
        """ Number of desimals in stored data. """
        LineValidator.is_not_None( self._keyword, decimals)
        LineValidator.is_int( self._keyword, decimals)
        LineValidator.in_range(0,15, self._keyword, decimals)
        my_value = _PxInt(decimals)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> int:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

