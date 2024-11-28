﻿from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeVariableLang
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Domain(_PxValueByKey):

    pxvalue_type: str = "_PxString"
    has_subkey: bool = True
    subkey_optional: bool = False
    completeness_type: str = "EachVariable"
    may_have_language: bool = True

    def __init__(self) -> None:
        super().__init__("DOMAIN")
        self._seen_languages = {}

    def set(self, code: str, domain: str, variable: str, lang: str = None) -> None:
        """Can occur once for each variable. Is used to determine which value sets are of interest, and thus which aggregation lists can be used."""
        LineValidator.is_not_None(self._keyword, domain)
        LineValidator.is_string(self._keyword, domain)
        my_value = _PxString(domain)
        my_key = _KeytypeVariableLang(variable, lang, code)
        try:
            super().set(my_value, my_key)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang] = 1

    def get_value(self, variable: str, lang: str = None) -> str:
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
