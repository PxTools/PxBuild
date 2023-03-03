from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeValuesLangMulti
from pxtool.model.util._line_validator import LineValidator

class _Datanotecell(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = True

    def __init__(self, keyword:str) -> None:
        super().__init__(keyword)
        self.occurence_counter = 0

    def set(self, datanotecell:str, values:list[str], lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, datanotecell)
        LineValidator.is_string( self._keyword, datanotecell)
        my_value = _PxString(datanotecell)
        self.occurence_counter += 1
        my_key = _KeytypeValuesLangMulti(values, lang, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeValuesLangMulti) -> _PxString:
        return super().get_value(my_key)