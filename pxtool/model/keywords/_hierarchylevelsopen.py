from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Hierarchylevelsopen(_PxValueByKey): 

    pxvalue_type:str = "_PxInt"
    may_have_language:bool = True


    def set(self, hierarchylevelsopen:int, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, hierarchylevelsopen)
        LineValidator.is_int( self._keyword, hierarchylevelsopen)
        my_value = _PxInt(hierarchylevelsopen)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableLang) -> _PxInt:
        return super().get_value(my_key)