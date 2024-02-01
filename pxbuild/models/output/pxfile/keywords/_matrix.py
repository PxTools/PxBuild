from pxbuild.models.output.pxfile.util._px_super import _PxSingle
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Matrix(_PxSingle):

    pxvalue_type: str = "_PxString"
    has_subkey: bool = False
    subkey_optional: bool = False
    completeness_type: str = ""
    may_have_language: bool = False

    def __init__(self) -> None:
        super().__init__("MATRIX")

    def set(self, matrix: str) -> None:
        """The name of the matrix. Is suggested as file name when the file is fetched."""
        LineValidator.is_not_None(self._keyword, matrix)
        LineValidator.is_string(self._keyword, matrix)
        my_value = _PxString(matrix)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()
