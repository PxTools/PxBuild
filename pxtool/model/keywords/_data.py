from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxData
from pxtool.model.util._line_validator import LineValidator

class _Data(_PxSingle): 

    pxvalue_type:str = "_PxData"
    may_have_language:bool = False


    def set(self, data:list) -> None:
        """  """
        my_value = _PxData(data)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> _PxData:
        return super().get_value()

