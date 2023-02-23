from pxtool.model.util._px_super import _PXSingle, _PxBool
from pxtool.model.util._line_validator import LineValidator

class _PX_DESCRIPTIONDEFAULT(_PXSingle): 

    def set(self, descriptiondefault:bool) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, descriptiondefault)
        LineValidator.is_bool( self._keyword, descriptiondefault)
        my_value = _PxBool(descriptiondefault)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

