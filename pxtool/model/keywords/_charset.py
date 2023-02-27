from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_CHARSET(_PXSingle): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = False


    def set(self, charset:str) -> None:
        """ Not in use """
        LineValidator.is_not_None( self._keyword, charset)
        LineValidator.is_string( self._keyword, charset)
        my_value = _PxString(charset)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

