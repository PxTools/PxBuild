from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._line_validator import LineValidator

class _Aggregallowed(_PxSingle): 

    pxvalue_type:str = "_PxBool"
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("AGGREGALLOWED")

    def set(self, aggregallowed:bool) -> None:
        """ False if the contents of the table cannot be aggregated """
        LineValidator.is_not_None( self._keyword, aggregallowed)
        LineValidator.is_bool( self._keyword, aggregallowed)
        my_value = _PxBool(aggregallowed)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> bool:
        return super().get_value().get_value()

