from pxtool.model.util._px_super import _PXValueByKey, _PxTlist
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_TIMEVAL(_PXValueByKey): 

    pxvalue_type:str = _PxTlist
    is_language_dependent:bool = True


    def set(self, timescale:str, time_periods:list[str], variable:str, lang:str = None) -> None:
        """ TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”;  """
        my_value = _PxTlist(timescale, time_periods)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

