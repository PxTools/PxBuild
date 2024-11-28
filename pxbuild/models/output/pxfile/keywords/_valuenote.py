﻿from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeVariableValueLangMulti
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


class _Valuenote(_PxValueByKey):

    pxvalue_type: str = "_PxString"
    has_subkey: bool = True
    subkey_optional: bool = False
    completeness_type: str = ""
    may_have_language: bool = True

    def __init__(self) -> None:
        super().__init__("VALUENOTE")
        self._seen_languages = {}
        self.occurence_counter = 0

    def set(self, code: str, valuenote: str, variable: str, value: str, lang: str = None) -> None:
        """Non-mandatory footnote for value in variable"""
        LineValidator.is_not_None(self._keyword, valuenote)
        LineValidator.is_string(self._keyword, valuenote)
        my_value = _PxString(valuenote)
        self.occurence_counter += 1
        my_key = _KeytypeVariableValueLangMulti(variable, value, lang, self.occurence_counter, code)
        try:
            super().set(my_value, my_key)
        except Exception as e:
            msg = self._keyword + ":" + str(e)
            raise type(e)(msg) from e
        self._seen_languages[lang] = 1

    def get_value(self, variable: str, value: str, lang: str = None) -> str:
        # TODO how should this function? Any usecases?
        my_key = _KeytypeVariableValueLangMulti(variable, value, lang, 1)
        return super().get_value(my_key).get_value()

    def has_value(self, variable: str, value: str, lang: str = None) -> bool:
        # TODO how should this function? Any usecases?
        my_key = _KeytypeVariableValueLangMulti(variable, value, lang, 1)
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
