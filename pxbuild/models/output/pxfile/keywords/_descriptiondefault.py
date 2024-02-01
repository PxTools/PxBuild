from pxbuild.models.output.pxfile.util._px_super import _PxSingle
from pxbuild.models.output.pxfile.util._px_valuetype import _PxBool
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Descriptiondefault(_PxSingle):

    pxvalue_type: str = "_PxBool"
    has_subkey: bool = False
    subkey_optional: bool = False
    completeness_type: str = ""
    may_have_language: bool = False

    def __init__(self) -> None:
        super().__init__("DESCRIPTIONDEFAULT")

    def set(self, descriptiondefault: bool) -> None:
        """Not in normal use."""
        LineValidator.is_not_None(self._keyword, descriptiondefault)
        LineValidator.is_bool(self._keyword, descriptiondefault)
        my_value = _PxBool(descriptiondefault)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e

    def get_value(self) -> bool:
        return super().get_value().get_value()

    def has_value(self) -> bool:
        return super().has_value()
