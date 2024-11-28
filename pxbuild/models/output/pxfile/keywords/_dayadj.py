﻿from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxBool
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeContentLang
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Dayadj(_PxValueByKey):

    pxvalue_type: str = "_PxBool"
    has_subkey: bool = True
    subkey_optional: bool = False
    completeness_type: str = "AllContent"
    may_have_language: bool = True

    def __init__(self) -> None:
        super().__init__("DAYADJ")
        self._seen_languages = {}

    def set(self, code: str, dayadj: bool, content: str = None, lang: str = None) -> None:
        """data is adjusted e.g. to take into account the number of working days"""
        LineValidator.is_not_None(self._keyword, dayadj)
        LineValidator.is_bool(self._keyword, dayadj)
        my_value = _PxBool(dayadj)
        my_key = _KeytypeContentLang(content, lang, code)
        try:
            super().set(my_value, my_key)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang] = 1

    def get_value(self, content: str = None, lang: str = None) -> bool:
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
