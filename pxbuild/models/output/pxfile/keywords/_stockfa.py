﻿from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeContentLang
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Stockfa(_PxValueByKey):

    pxvalue_type: str = "_PxString"
    has_subkey: bool = True
    subkey_optional: bool = False
    completeness_type: str = "AllContent"
    may_have_language: bool = True

    def __init__(self) -> None:
        super().__init__("STOCKFA")
        self._seen_languages = {}

    def set(self, stockfa: str, content: str = None, lang: str = None) -> None:
        """Indicates if data is stock, flow or average.  Used characters: S (stock), F (flow) and A (average)"""
        LineValidator.is_not_None(self._keyword, stockfa)
        LineValidator.is_string(self._keyword, stockfa)
        LineValidator.regexp_string("^(S|F|A)$", self._keyword, stockfa)
        my_value = _PxString(stockfa)
        my_key = _KeytypeContentLang(content, lang)
        try:
            super().set(my_value, my_key)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang] = 1

    def get_value(self, content: str = None, lang: str = None) -> str:
        my_key = _KeytypeContentLang(content, lang)
        return super().get_value(my_key).get_value()

    def has_value(self, content: str = None, lang: str = None) -> bool:
        my_key = _KeytypeContentLang(content, lang)
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
