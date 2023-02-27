from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._line_validator import LineValidator

class _PX_SHOWDECIMALS(_PXSingle): 

    pxvalue_type:str = "int"
    is_language_dependent:bool = False


    def set(self, showdecimals:int) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, showdecimals)
        LineValidator.is_int( self._keyword, showdecimals)
        LineValidator.in_range(0,6, self._keyword, showdecimals)
        my_value = int(showdecimals)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

