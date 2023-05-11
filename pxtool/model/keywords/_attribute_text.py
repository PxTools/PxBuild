from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _AttributeText(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    has_subkey:bool = False
    subkey_optional:bool = False
    may_have_language:bool = True
    _seen_languages={}

    def __init__(self) -> None:
        super().__init__("ATTRIBUTE-TEXT")

    def set(self, attribute_text:list[str], lang:str = None) -> None:
        """ Not in normal use. See pdf """
        LineValidator.is_not_None( self._keyword, attribute_text)
        LineValidator.is_list_of_strings( self._keyword, attribute_text)
        my_value = _PxStringList(attribute_text)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, lang:str = None) -> list[str]:
        my_key = _KeytypeLang(lang)
        return super().get_value(my_key).get_value()

    def has_value(self, lang:str = None) -> bool:
        my_key = _KeytypeLang(lang)
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
