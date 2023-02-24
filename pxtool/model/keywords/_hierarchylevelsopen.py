from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_HIERARCHYLEVELSOPEN(_PXValueByKey): 

    pxvalue_type:str = int
    is_language_dependent:bool = True


    def set(self, hierarchylevelsopen:int, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, hierarchylevelsopen)
        LineValidator.is_int( self._keyword, hierarchylevelsopen)
        my_value = int(hierarchylevelsopen)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

