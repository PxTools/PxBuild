from pxtool.model.util._px_super import _PXValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_VARIABLE_CODE(_PXValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, variable_code:str, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, variable_code)
        LineValidator.is_string( self._keyword, variable_code)
        my_value = _PxString(variable_code)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

