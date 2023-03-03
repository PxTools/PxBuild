from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _Stub(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    may_have_language:bool = True


    def set(self, stub:list[str], lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, stub)
        LineValidator.is_list_of_strings( self._keyword, stub)
        my_value = _PxStringList(stub)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeLang) -> _PxStringList:
        return super().get_value(my_key)