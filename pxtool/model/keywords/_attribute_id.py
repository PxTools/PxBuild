from pxtool.model.util._px_super import _PXSingle, _PxStringList
from pxtool.model.util._line_validator import LineValidator

class _PX_ATTRIBUTE_ID(_PXSingle): 

    def set(self, attribute_id:list[str]) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, attribute_id)
        LineValidator.is_list_of_strings( self._keyword, attribute_id)
        my_value = _PxStringList(attribute_id)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

