from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_LANGUAGE(_PXSingle): 

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

