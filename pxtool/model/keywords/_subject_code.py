from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _SubjectCode(_PxSingle): 

    pxvalue_type:str = "_PxString"
    has_subkey:bool = False
    subkey_optional:bool = False
    completeness_type:str = ""
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("SUBJECT-CODE")

    def set(self, subject_code:str) -> None:
        """ Subject area code. It is used to create files with tables available in PC-Axis. The text must not exceed 20 characters  """
        LineValidator.is_not_None( self._keyword, subject_code)
        LineValidator.is_string( self._keyword, subject_code)
        my_value = _PxString(subject_code)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()

