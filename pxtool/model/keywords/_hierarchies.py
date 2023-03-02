from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxHierarchy
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Hierarchies(_PxValueByKey): 

    pxvalue_type:str = "_PxHierarchy"
    is_language_dependent:bool = True


    def set(self, root_node:str, mother_child:dict[str,str], variable:str, lang:str = None) -> None:
        """  """
        my_value = _PxHierarchy(root_node, mother_child)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableLang) -> _PxHierarchy:
        return super().get_value(my_key)