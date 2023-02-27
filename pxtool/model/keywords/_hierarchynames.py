from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_HIERARCHYNAMES(_PXValueByKey): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = True


    def set(self, hierarchynames:list[str], variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, hierarchynames)
        LineValidator.is_list_of_strings( self._keyword, hierarchynames)
        my_value = _PxStringList(hierarchynames)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

