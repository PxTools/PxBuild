from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeLang
from pxtool.model.util._line_validator import LineValidator

class _SubjectArea(_PxValueByKey): 

    pxvalue_type:str = "_PxString"
    is_language_dependent:bool = True


    def set(self, subject_area:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, subject_area)
        LineValidator.is_string( self._keyword, subject_area)
        my_value = _PxString(subject_area)
        my_key = _KeytypeLang(lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeLang) -> _PxString:
        return super().get_value(my_key)