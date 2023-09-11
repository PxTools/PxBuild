from pxtool.models.output.pxfile.util._px_super import _PxSingle
from pxtool.models.output.pxfile.util._px_valuetype import _PxString
from pxtool.models.output.pxfile.util._line_validator import LineValidator

class _Language(_PxSingle): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("LANGUAGE")

    def set(self, language:str) -> None:
        """ Language-code with 2 letters,sv for Swedish, en for English etc. Default language """
        LineValidator.is_not_None( self._keyword, language)
        LineValidator.is_string( self._keyword, language)
        LineValidator.regexp_string("^[a-z]{2}$", self._keyword, language)
        my_value = _PxString(language)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

