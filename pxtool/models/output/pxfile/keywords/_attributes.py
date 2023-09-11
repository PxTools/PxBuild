from pxtool.models.output.pxfile.util._px_super import _PxValueByKey
from pxtool.models.output.pxfile.util._px_valuetype import _PxStringList
from pxtool.models.output.pxfile.util._px_keytypes import _KeytypeCodes
from pxtool.models.output.pxfile.util._line_validator import LineValidator

class _Attributes(_PxValueByKey): 

    pxvalue_type:str = "_PxStringList"
    has_subkey:bool = True
    subkey_optional:bool = True
    completeness_type:str = "TODO"
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("ATTRIBUTES")

    def set(self, attributes:list[str], codes:list[str]=None) -> None:
        """ Not in normal use. See pdf """
        LineValidator.is_not_None( self._keyword, attributes)
        LineValidator.is_list_of_strings( self._keyword, attributes)
        my_value = _PxStringList(attributes)
        my_key = _KeytypeCodes(codes)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, codes:list[str]=None) -> list[str]:
        my_key = _KeytypeCodes(codes)
        return super().get_value(my_key).get_value()

    def has_value(self, codes:list[str]=None) -> bool:
        my_key = _KeytypeCodes(codes)
        return super().has_value(my_key)

