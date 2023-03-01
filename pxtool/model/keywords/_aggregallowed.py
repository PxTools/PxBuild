from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._line_validator import LineValidator

class _Aggregallowed(_PxSingle): 

    pxvalue_type:str = "_PxBool"
    is_language_dependent:bool = False


    def set(self, aggregallowed:bool) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, aggregallowed)
        LineValidator.is_bool( self._keyword, aggregallowed)
        my_value = _PxBool(aggregallowed)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

