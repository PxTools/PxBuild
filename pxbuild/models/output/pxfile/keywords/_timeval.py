﻿from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxTlist
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeVariableLang
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Timeval(_PxValueByKey):

    pxvalue_type: str = "_PxTlist"
    has_subkey: bool = True
    subkey_optional: bool = False
    completeness_type: str = "OneVariable"
    may_have_language: bool = True

    def __init__(self) -> None:
        super().__init__("TIMEVAL")
        self._seen_languages = {}

    def set(self, code: str, timescale: str, time_periods: list[str], variable: str, lang: str = None) -> None:
        """See pdf. TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”;"""
        my_value = _PxTlist(timescale, time_periods)
        my_key = _KeytypeVariableLang(variable, lang, code)
        try:
            super().set(my_value, my_key)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang] = 1

    def get_value(self, variable: str, lang: str = None) -> (str, list[str]):
        my_key = _KeytypeVariableLang(variable, lang)
        return super().get_value(my_key).get_value()

    def has_value(self, variable: str, lang: str = None) -> bool:
        my_key = _KeytypeVariableLang(variable, lang)
        return super().has_value(my_key)

    def get_used_languages(self) -> list[str]:
        return list(self._seen_languages.keys())

    def reset_language_none_to(self, lang: str) -> None:
        if not lang:
            return
        if None in self.get_used_languages():
            super().reset_language_none_to(lang)
            # unsee None
            del self._seen_languages[None]
            self._seen_languages[lang] = 1
