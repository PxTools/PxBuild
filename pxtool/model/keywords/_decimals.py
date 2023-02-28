from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._line_validator import LineValidator

class _PX_DECIMALS(_PXSingle): 

    pxvalue_type:str = "_PxInt"
    is_language_dependent:bool = False


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

