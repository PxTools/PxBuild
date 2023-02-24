from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_TABLEID(_PXSingle): 

    pxvalue_type:str = _PxString
    is_language_dependent:bool = False


    def set(self, tableid:str) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, tableid)
        LineValidator.is_string( self._keyword, tableid)
        my_value = _PxString(tableid)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

