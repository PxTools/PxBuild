from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._line_validator import LineValidator

class _Copyright(_PxSingle): 

    pxvalue_type:str = "_PxBool"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("COPYRIGHT")

    def set(self, copyright:bool) -> None:
        """ If true the copyright refers to the organization given in SOURCE """
        LineValidator.is_not_None( self._keyword, copyright)
        LineValidator.is_bool( self._keyword, copyright)
        my_value = _PxBool(copyright)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> bool:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

