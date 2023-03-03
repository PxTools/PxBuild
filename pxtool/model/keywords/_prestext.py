from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxInt
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Prestext(_PxValueByKey): 

    pxvalue_type:str = "_PxInt"
    may_have_language:bool = True
    _seen_languages={}


    def set(self, prestext:int, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, prestext)
        LineValidator.is_int( self._keyword, prestext)
        LineValidator.in_range(0,3, self._keyword, prestext)
        my_value = _PxInt(prestext)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, my_key: _KeytypeVariableLang) -> _PxInt:
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
