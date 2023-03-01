from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxStringList
from pxtool.model.util._px_keytypes import _keytype_lang
from pxtool.model.util._line_validator import LineValidator

class AttributeText(_PXValueByKey): 

    pxvalue_type:str = "_PxStringList"
    is_language_dependent:bool = True


    def set(self, attribute_text:list[str], lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, attribute_text)
        LineValidator.is_list_of_strings( self._keyword, attribute_text)
        my_value = _PxStringList(attribute_text)
        my_key = _keytype_lang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

