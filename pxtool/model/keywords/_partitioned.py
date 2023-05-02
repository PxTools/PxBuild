from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _KeytypeVariableLangMulti
from pxtool.model.util._line_validator import LineValidator

class _Partitioned(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    may_have_language:bool = True
    _seen_languages={}

    def __init__(self) -> None:
        super().__init__("PARTITIONED")
        self.occurence_counter = 0

    def set(self, partitioned:list[str], variable:str, lang:str = None) -> None:
        """ string , int (,int) , see pdf """
        LineValidator.is_not_None( self._keyword, partitioned)
        LineValidator.is_list_of_strings( self._keyword, partitioned)
        my_value = _PxStringList(partitioned)
        self.occurence_counter += 1
        my_key = _KeytypeVariableLangMulti(variable, lang, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang]=1

    def get_value(self, variable:str, lang:str = None) -> list[str]:
        #TODO how should this function? Any usecases?
        my_key = _KeytypeVariableLangMulti(variable, lang,1)
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
