from pxtool.models.output.pxfile.util._px_super import _PxSingle
from pxtool.models.output.pxfile.util._px_valuetype import _PxString
from pxtool.models.output.pxfile.util._line_validator import LineValidator

class _Codepage(_PxSingle): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("CODEPAGE")

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

    def has_value(self) -> bool:
        return super().has_value()

