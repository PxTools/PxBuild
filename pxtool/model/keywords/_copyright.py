from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._line_validator import LineValidator

class _PX_COPYRIGHT(_PXSingle): 

    pxvalue_type:str = "_PxBool"
    is_language_dependent:bool = False


    def set(self, copyright:bool) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, copyright)
        LineValidator.is_bool( self._keyword, copyright)
        my_value = _PxBool(copyright)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

