from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _KeytypeValuesMulti
from pxtool.model.util._line_validator import LineValidator

class _Attributes(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    has_subkey:bool = True
    subkey_optional:bool = True
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("ATTRIBUTES")
        self.occurence_counter = 0

    def set(self, attributes:list[str], values:list[str]=None) -> None:
        """ Not in normal use. See pdf """
        LineValidator.is_not_None( self._keyword, attributes)
        LineValidator.is_list_of_strings( self._keyword, attributes)
        my_value = _PxStringList(attributes)
        self.occurence_counter += 1
        my_key = _KeytypeValuesMulti(values, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, values:list[str]=None) -> list[str]:
        #TODO how should this function? Any usecases?
        my_key = _KeytypeValuesMulti(values,1)
        return super().get_value(my_key).get_value()

    def has_value(self, values:list[str]=None) -> bool:
        #TODO how should this function? Any usecases?
        my_key = _KeytypeValuesMulti(values,1)
        return super().has_value(my_key)

