from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._line_validator import LineValidator

class _PX_SYNONYMS(_PXSingle): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = False


    def set(self, synonyms:list[str]) -> None:
        """ This is used for search in PX-Web. If the table concerns CPI the synonym 
can be “Inflation”. Several words can be included """
        LineValidator.is_not_None( self._keyword, synonyms)
        LineValidator.is_list_of_strings( self._keyword, synonyms)
        my_value = _PxStringList(synonyms)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

