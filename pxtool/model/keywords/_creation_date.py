from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _CreationDate(_PxSingle): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("CREATION-DATE")

    def set(self, creation_date:str) -> None:
        """ Date in 'Px Format' """
        LineValidator.is_not_None( self._keyword, creation_date)
        LineValidator.is_string( self._keyword, creation_date)
        my_value = _PxString(creation_date)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

