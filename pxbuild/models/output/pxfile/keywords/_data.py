from pxbuild.models.output.pxfile.util._px_super import _PxSingle
from pxbuild.models.output.pxfile.util._px_valuetype import _PxData
from pxbuild.models.output.pxfile.util._line_validator import LineValidator

class _Data(_PxSingle): 

    pxvalue_type:str = "_PxData"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("DATA")

    def set(self, data:list, columns_per_line:int) -> None:
        """ Numbers and quoted dots """
        my_value = _PxData(data, columns_per_line)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> list:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

