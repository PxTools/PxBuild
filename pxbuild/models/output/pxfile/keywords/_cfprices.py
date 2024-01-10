from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeContentLang
from pxbuild.models.output.pxfile.util._line_validator import LineValidator

class _Cfprices(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = True
    subkey_optional:bool = False
    completeness_type:str = "AllContent"
    may_have_language:bool = True

    def __init__(self) -> None:
        super().__init__("CFPRICES")
        self._seen_languages={}

    def set(self, cfprices:str, content:str=None, lang:str = None) -> None:
        """ Indicates if data is in current or fixed prices. C is used for Current and F for Fixed prices """
        LineValidator.is_not_None( self._keyword, cfprices)
        LineValidator.is_string( self._keyword, cfprices)
        LineValidator.regexp_string("^(C|F)$", self._keyword, cfprices)
        my_value = _PxString(cfprices)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, content:str=None, lang:str = None) -> str:
        my_key = _KeytypeContentLang(content, lang)
        return super().get_value(my_key).get_value()

    def has_value(self, content:str=None, lang:str = None) -> bool:
        my_key = _KeytypeContentLang(content, lang)
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
