from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._line_validator import LineValidator

class AttributeId(_PXSingle): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = False


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

