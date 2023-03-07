from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _Source(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = True
    _seen_languages={}


    def set(self, source:str, lang:str = None) -> None:
        """ States the organization which is responsible for the statistics """
        LineValidator.is_not_None( self._keyword, source)
        LineValidator.is_string( self._keyword, source)
        my_value = _PxString(source)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, my_key: _KeytypeLang) -> _PxString:
        return super().get_value(my_key)

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
