from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._line_validator import LineValidator

class _Languages(_PxSingle): 

    pxvalue_type:str = "_PxStringList"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("LANGUAGES")

    def set(self, languages:list[str]) -> None:
        """ List of Language-codes used in file. """
        LineValidator.is_not_None( self._keyword, languages)
        LineValidator.is_list_of_strings( self._keyword, languages)
        LineValidator.regexp_item_string("^[a-z]{2}$", self._keyword, languages)
        LineValidator.unique( self._keyword, languages)
        my_value = _PxStringList(languages)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> list[str]:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

