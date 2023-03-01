from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._line_validator import LineValidator

class Confidential(_PXSingle): 

    pxvalue_type:str = "_PxInt"
    is_language_dependent:bool = False


    def set(self, confidential:int) -> None:
        """ Never put confidential data in a pxfile. Ever. Not in use. """
        LineValidator.is_not_None( self._keyword, confidential)
        LineValidator.is_int( self._keyword, confidential)
        my_value = _PxInt(confidential)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

