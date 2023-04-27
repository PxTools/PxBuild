from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _Codepage(_PxSingle): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = False


    def set(self, codepage:str) -> None:
        """ Not in use """
        LineValidator.is_not_None( self._keyword, codepage)
        LineValidator.is_string( self._keyword, codepage)
        my_value = _PxString(codepage)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

