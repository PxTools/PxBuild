from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Codes(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = True


    def set(self, codes:list[str], variable:str, lang:str = None) -> None:
        """ Hei fra kolonne J,Codes """
        LineValidator.is_not_None( self._keyword, codes)
        LineValidator.is_list_of_strings( self._keyword, codes)
        LineValidator.unique( self._keyword, codes)
        my_value = _PxStringList(codes)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

