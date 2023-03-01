from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxHierarchy
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class Hierarchies(_PXValueByKey): 

    pxvalue_type:str = "_PxHierarchy"
    is_language_dependent:bool = True


    def set(self, root_node:str, mother_child:dict[str,str], variable:str, lang:str = None) -> None:
        """  """
        my_value = _PxHierarchy(root_node, mother_child)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

