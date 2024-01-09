from pxbuild.models.output.pxfile.util._px_super import _PxSingle
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._line_validator import LineValidator

class _NextUpdate(_PxSingle): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("NEXT-UPDATE")

    def set(self, next_update:str) -> None:
        """ Not in use. Date in 'Px  format' """
        LineValidator.is_not_None( self._keyword, next_update)
        LineValidator.is_string( self._keyword, next_update)
        my_value = _PxString(next_update)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

