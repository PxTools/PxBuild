from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _keytype_values_multi
from pxtool.model.util._line_validator import LineValidator

class _PX_ATTRIBUTES(_PXValueByKey): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = False

    def __init__(self, keyword:str) -> None:
        super().__init__(keyword)
        self.occurence_counter = 0

    def set(self, attributes:list[str], values:list[str]) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, attributes)
        LineValidator.is_list_of_strings( self._keyword, attributes)
        my_value = _PxStringList(attributes)
        self.occurence_counter += 1
        my_key = _keytype_values_multi(values, self.occurence_counter)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

