from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._px_keytypes import _KeytypeContentLang
from pxtool.model.util._line_validator import LineValidator

class _Seasadj(_PxValueByKey): 

    pxvalue_type:str = "_PxBool"
    is_language_dependent:bool = True


    def set(self, seasadj:bool, content:str=None, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, seasadj)
        LineValidator.is_bool( self._keyword, seasadj)
        my_value = _PxBool(seasadj)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeContentLang) -> _PxBool:
        return super().get_value(my_key)