from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Hierarchylevelsopen(_PxValueByKey): 

    pxvalue_type:str = "_PxInt"
    may_have_language:bool = True
    _seen_languages={}

    def __init__(self) -> None:
        super().__init__("HIERARCHYLEVELSOPEN")

    def set(self, hierarchylevelsopen:int, variable:str, lang:str = None) -> None:
        """ Not in normal use. See pdf """
        LineValidator.is_not_None( self._keyword, hierarchylevelsopen)
        LineValidator.is_int( self._keyword, hierarchylevelsopen)
        my_value = _PxInt(hierarchylevelsopen)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, variable:str, lang:str = None) -> int:
        my_key = _KeytypeVariableLang(variable, lang)
        return super().get_value(my_key).get_value()

    def get_used_languages(self) -> list[str]:
       return list(self._seen_languages.keys())

    def reset_language_none_to(self,lang:str)->None:
        if not lang:
            return
        if None in self.get_used_languages():
             super().reset_language_none_to(lang)
             #unsee None
             del self._seen_languages[None]
             self._seen_languages[lang]=1
