from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _Matrix(_PxSingle): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = False


    def set(self, matrix:str) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, matrix)
        LineValidator.is_string( self._keyword, matrix)
        my_value = _PxString(matrix)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> _PxString:
        return super().get_value()