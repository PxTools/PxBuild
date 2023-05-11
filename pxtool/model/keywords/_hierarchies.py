from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxHierarchy
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Hierarchies(_PxValueByKey): 

    pxvalue_type:str = "_PxHierarchy"
    has_subkey:bool = True
    subkey_optional:bool = False
    may_have_language:bool = True
    _seen_languages={}

    def __init__(self) -> None:
        super().__init__("HIERARCHIES")

    def set(self, root_node:str, mother_child:dict[str,str], variable:str, lang:str = None) -> None:
        """ Not in normal use. See pdf """
        my_value = _PxHierarchy(root_node, mother_child)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, variable:str, lang:str = None) -> (str, dict[str,str]):
        my_key = _KeytypeVariableLang(variable, lang)
        return super().get_value(my_key).get_value()

    def has_value(self, variable:str, lang:str = None) -> bool:
        my_key = _KeytypeVariableLang(variable, lang)
        return super().has_value(my_key)

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
