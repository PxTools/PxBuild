from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _Datasymbol3(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, datasymbol3:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, datasymbol3)
        LineValidator.is_string( self._keyword, datasymbol3)
        my_value = _PxString(datasymbol3)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

