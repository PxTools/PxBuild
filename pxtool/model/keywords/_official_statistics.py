from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._line_validator import LineValidator

class _OfficialStatistics(_PxSingle): 

    pxvalue_type:str = "_PxBool"
    may_have_language:bool = False


    def set(self, official_statistics:bool) -> None:
        """ Indicates if the data table is included in the official statistics of the organization. """
        LineValidator.is_not_None( self._keyword, official_statistics)
        LineValidator.is_bool( self._keyword, official_statistics)
        my_value = _PxBool(official_statistics)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> _PxBool:
        return super().get_value()