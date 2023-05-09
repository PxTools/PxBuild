from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._line_validator import LineValidator

class _DefaultGraph(_PxSingle): 

    pxvalue_type:str = "_PxInt"
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("DEFAULT-GRAPH")

    def set(self, default_graph:int) -> None:
        """ Not in use """
        LineValidator.is_not_None( self._keyword, default_graph)
        LineValidator.is_int( self._keyword, default_graph)
        my_value = _PxInt(default_graph)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> int:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

