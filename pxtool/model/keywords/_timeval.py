from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxTlist
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Timeval(_PxValueByKey): 

    pxvalue_type:str = "_PxTlist"
    is_language_dependent:bool = True


    def set(self, timescale:str, time_periods:list[str], variable:str, lang:str = None) -> None:
        """ TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”;  """
        my_value = _PxTlist(timescale, time_periods)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self, my_key: _KeytypeVariableLang) -> _PxTlist:
        return super().get_value(my_key)