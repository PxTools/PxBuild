"""
These classes have 2 purposes:
  act as key in dictionary
  write the keypart nicely

They used to be just namedTuples, but we wanted to use pydantic for validation
"""

from ._line_validator import LineValidator


class _KeytypeLang:
    lang: str = None

    def __init__(self, lang: str) -> None:
        if lang:
            LineValidator.is_string("language in key", lang)
            LineValidator.regexp_string("^[a-z]{2}$", "language in key", lang)
        self.lang = lang

    def __str__(self):
        return f"[{self.lang}]" if self.lang else ""

    def __eq__(self, other):
        if type(self) is type(other):
            return self.lang == other.lang
        return False

    def __hash__(self):
        return hash(self.lang)

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeLang(lang)


class _KeytypeVariableLang(_KeytypeLang):
    variable: str

    def __init__(self, variable: str, lang: str) -> None:
        super().__init__(lang)
        self.variable = variable

    def __str__(self):
        if self.variable:
            return f'{super().__str__()}("{self.variable}")'
        else:
            return f"{super().__str__()}"

    def __eq__(self, other):
        if type(self) is type(other):
            return self.variable == other.variable and self.lang == other.lang
        return False

    def __hash__(self):
        return hash((self.variable, self.lang))

    def to_str_message(self) -> str:
        return f"for language '{self.lang}' and variable '{self.variable}'"

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeVariableLang(self.variable, lang)


class _KeytypeContentLang(_KeytypeLang):
    content: str

    def __init__(self, content: str, lang: str) -> None:
        super().__init__(lang)
        self.content = content

    def __str__(self):
        if self.content:
            return f'{super().__str__()}("{self.content}")'
        else:
            return f"{super().__str__()}"

    def __eq__(self, other):
        if type(self) is type(other):
            return self.content == other.content and self.lang == other.lang
        return False

    def __hash__(self):
        return hash((self.content, self.lang))

    def to_str_message(self) -> str:
        return f"for language '{self.lang}' and content '{self.content}'"

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeContentLang(self.content, lang)


class _KeytypeVariableValueLang(_KeytypeLang):
    variable: str
    value: str

    def __init__(self, variable: str, value: str, lang: str) -> None:
        super().__init__(lang)
        self.variable = variable
        self.value = value

    def __str__(self):
        if self.value:
            return f'{super().__str__()}("{self.variable}","{self.value}")'
        else:
            if self.variable:
                return f'{super().__str__()}("{self.variable}")'
            else:
                return f"{super().__str__()}"

    def __eq__(self, other):
        if type(self) is type(other):
            return self.variable == other.variable and self.value == other.value and self.lang == other.lang
        return False

    def __hash__(self):
        return hash((self.variable, self.value, self.lang))

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeVariableValueLang(self.variable, self.value, lang)


class _KeytypeVariableLangMulti(_KeytypeVariableLang):
    counter: int

    def __init__(self, variable: str, lang: str, counter: int) -> None:
        super().__init__(variable, lang)
        self.counter = counter

    def __eq__(self, other):
        if type(self) is type(other):
            return self.variable == other.variable and self.lang == other.lang and self.counter == other.counter
        return False

    def __hash__(self):
        return hash((self.variable, self.lang, self.counter))

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeVariableLangMulti(self.variable, lang, self.counter)


class _KeytypeVariableValueLangMulti(_KeytypeVariableValueLang):
    counter: int

    def __init__(self, variable: str, value: str, lang: str, counter: int) -> None:
        super().__init__(variable, value, lang)
        self.counter = counter

    def __eq__(self, other):
        if type(self) is type(other):
            return (
                self.variable == other.variable
                and self.value == other.value
                and self.lang == other.lang
                and self.counter == other.counter
            )
        return False

    def __hash__(self):
        return hash((self.variable, self.value, self.lang, self.counter))

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeVariableValueLangMulti(self.variable, self.value, lang, self.counter)


class _KeytypeValuesLangMulti(_KeytypeLang):
    values: list[str]
    counter: int
    _joined: str

    def __init__(self, values: list[str], lang: str, counter: int) -> None:
        super().__init__(lang)
        self.values = values
        self.counter = counter
        self._joined = '","'.join(self.values) if values else "TODO"

    def __str__(self):
        return f'{super().__str__()}("{self._joined}")'

    def __eq__(self, other):
        if type(self) is type(other):
            return self._joined == other._joined and self.lang == other.lang and self.counter == other.counter
        return False

    def __hash__(self):
        return hash((self._joined, self.lang, self.counter))

    def reset_lang_none_to(self, lang: str):
        if self.lang:
            return self
        else:
            return _KeytypeValuesLangMulti(self.values, lang, self.counter)


class _KeytypeCodes:
    codes: list[str]
    _joined: str

    def __init__(self, codes: list[str]) -> None:
        super().__init__()
        self.codes = codes
        self._joined = '","'.join(self.codes)

    def __str__(self):
        return f'("{self._joined}")'

    def __eq__(self, other):
        if type(self) is type(other):
            return self._joined == other._joined
        return False

    def __hash__(self):
        return hash(self._joined)
