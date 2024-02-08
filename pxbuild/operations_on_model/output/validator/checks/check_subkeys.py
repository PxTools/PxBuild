from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey
from pxbuild.models.output.pxfile.util._px_keytypes import (
    _KeytypeVariableLang,
    _KeytypeContentLang,
    _KeytypeVariableValueLang,
    _KeytypeValuesLangMulti,
    _KeytypeCodes,
)

from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult
import pxbuild.models.output.pxfile.util.constants as const


class _Checker:
    def __init__(self, model: PXFileModel) -> None:
        self.val_result = ValidationResult(
            desc="Check if the values found in any subkey are valid. And that values-subkeytype has all variables."
        )
        self.error_intro = ""
        self.model = model

        for keyword_name in const.KEYWORDS_PYTHONIC_MAP:
            keyword = model.get_attribute(const.KEYWORDS_PYTHONIC_MAP[keyword_name])
            if keyword.is_present() and keyword.has_subkey:
                for key in keyword._value_by_key:
                    self.error_intro = f"For keyword {keyword._keyword}"

                    if type(key) is _KeytypeContentLang:
                        self.check_keytype_content(key, keyword)
                    elif isinstance(key, _KeytypeVariableLang):
                        self.check_keytype_variable(key, keyword)
                    elif isinstance(key, _KeytypeVariableValueLang):
                        self.check_keytype_variable_value(key, keyword)
                    elif type(key) is _KeytypeValuesLangMulti:
                        self.check_keytype_values(key, keyword)
                    elif type(key) is _KeytypeCodes:
                        # Not valuebased
                        pass
                    else:  # pragma: no cover
                        self.val_result.add_error(
                            f"{self.error_intro}: Sorry, bug in app. Unhandled keytype:{type(key)}. For lang:{key.lang}."
                        )

    def check_keytype_values(self, key: _KeytypeValuesLangMulti, keyword: _PxValueByKey) -> None:
        if not key.values:
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Values can not be None. For lang:{key.lang}.")
        else:
            dimensions = self.model.stub.get_value(key.lang) + self.model.heading.get_value(key.lang)
            if not len(dimensions) == len(key.values):
                self.val_result.add_error(
                    f"{self.error_intro}: There are {len(dimensions)} dimensions, but {len(key.values)} values. For lang:{key.lang}."
                )
            else:
                dimension_cnt = -1
                for value in key.values:
                    dimension_cnt += 1
                    if value == "*":
                        continue
                    self.check_if_value_in_values(key.lang, dimensions[dimension_cnt], value, self.model)

    def check_keytype_variable(self, key: _KeytypeVariableLang, keyword: _PxValueByKey) -> None:
        if not key.variable:
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Variable can not be None. For lang:{key.lang}.")
        else:
            self.check_variable_in_stub_or_heading(key.lang, key.variable, self.model)

    def check_keytype_variable_value(self, key: _KeytypeVariableValueLang, keyword: _PxValueByKey) -> None:
        if not key.variable:
            if key.value:
                self.val_result.add_error(f"{self.error_intro}: Found value, but no variable . For lang:{key.lang}.")
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Variable can not be None. For lang:{key.lang}.")
        else:
            if not key.value:
                if not keyword.subkey_optional:
                    self.val_result.add_error(
                        f"{self.error_intro}: Need value for variable {key.variable}. For lang:{key.lang}."
                    )
            else:
                if self.check_variable_in_stub_or_heading(key.lang, key.variable, self.model):
                    self.check_if_value_in_values(key.lang, key.variable, key.value, self.model)

    def check_keytype_content(self, key: _KeytypeContentLang, keyword: _PxValueByKey) -> None:
        if not key.content:
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Content value can not be None. For lang:{key.lang}.")
        else:
            self.check_if_value_in_values(
                key.lang, self.model.contvariable.get_value(key.lang), key.content, self.model
            )

    def check_if_value_in_values(self, lang: str, dimension: str, value: str, model: PXFileModel) -> bool:
        my_out = value in model.values.get_value(dimension, lang)
        if not my_out:
            self.val_result.add_error(
                f"{self.error_intro}: Cannot find item {value} in VALUES for vaiable:{dimension} and lang:{lang}."
            )
        return my_out

    def check_variable_in_stub_or_heading(self, lang: str, variable: str, model: PXFileModel) -> bool:
        my_out = variable in model.stub.get_value(lang) + model.heading.get_value(lang)
        if not my_out:
            self.val_result.add_error(
                f"{self.error_intro}: Cannot find variable {variable} in stub + heading. For lang:{lang}."
            )
        return my_out


def check_valuebased_subkeys(model: PXFileModel) -> ValidationResult:
    return _Checker(model).val_result
