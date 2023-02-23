from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_SUBJECT_CODE(_PXSingle): 

    def set(self, subject_code:str) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, subject_code)
        LineValidator.is_string( self._keyword, subject_code)
        my_value = _PxString(subject_code)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

