from pxtool.model.util._px_super import _PXSingle, _PxStringList
from pxtool.model.util._line_validator import LineValidator

class _PX_LANGUAGES(_PXSingle): 

    pxvalue_type:str = _PxStringList
    is_language_dependent:bool = False


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

