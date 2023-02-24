from pxtool.model.util._px_super import _PXSingle, _PxString
from pxtool.model.util._line_validator import LineValidator

class _PX_DIRECTORY_PATH(_PXSingle): 

    pxvalue_type:str = _PxString
    is_language_dependent:bool = False


    def set(self, directory_path:str) -> None:
        """ Not in use """
        LineValidator.is_not_None( self._keyword, directory_path)
        LineValidator.is_string( self._keyword, directory_path)
        my_value = _PxString(directory_path)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

