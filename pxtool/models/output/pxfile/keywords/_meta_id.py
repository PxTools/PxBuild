from pxtool.models.output.pxfile.util._px_super import _PxValueByKey
from pxtool.models.output.pxfile.util._px_valuetype import _PxString
from pxtool.models.output.pxfile.util._px_keytypes import _KeytypeVariableValueLang
from pxtool.models.output.pxfile.util._line_validator import LineValidator

class _MetaId(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = True
    subkey_optional:bool = True
    completeness_type:str = "EachVariable"
    may_have_language:bool = True

    def __init__(self) -> None:
        super().__init__("META-ID")
        self._seen_languages={}

    def set(self, meta_id:str, variable:str=None, value:str=None, lang:str = None) -> None:
        """ The META-ID keyword is used to reference a external meta information about a table, variable or value. Requires a separate file to resolve to urls """
        LineValidator.is_not_None( self._keyword, meta_id)
        LineValidator.is_string( self._keyword, meta_id)
        my_value = _PxString(meta_id)
        my_key = _KeytypeVariableValueLang(variable, value, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, variable:str=None, value:str=None, lang:str = None) -> str:
        my_key = _KeytypeVariableValueLang(variable, value, lang)
        return super().get_value(my_key).get_value()

    def has_value(self, variable:str=None, value:str=None, lang:str = None) -> bool:
        my_key = _KeytypeVariableValueLang(variable, value, lang)
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
