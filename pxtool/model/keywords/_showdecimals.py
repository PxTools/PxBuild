from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._line_validator import LineValidator

class Showdecimals(_PXSingle): 

    pxvalue_type:str = "_PxInt"
    is_language_dependent:bool = False


    def set(self, showdecimals:int) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, showdecimals)
        LineValidator.is_int( self._keyword, showdecimals)
        LineValidator.in_range(0,6, self._keyword, showdecimals)
        my_value = _PxInt(showdecimals)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

