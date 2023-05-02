from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._line_validator import LineValidator

class _Autopen(_PxSingle): 

    pxvalue_type:str = "_PxBool"
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("AUTOPEN")

    def set(self, autopen:bool) -> None:
        """ Not is use. """
        LineValidator.is_not_None( self._keyword, autopen)
        LineValidator.is_bool( self._keyword, autopen)
        my_value = _PxBool(autopen)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> bool:
        return super().get_value().get_value()

