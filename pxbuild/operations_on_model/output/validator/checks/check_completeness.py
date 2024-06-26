from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult
import pxbuild.models.output.pxfile.util.constants as const

from pxbuild.models.output.pxfile.util._px_super import _PxValueByKey


class _Checker:
    def __init__(self, model: PXFileModel) -> None:
        desc_part1: str = "Check if the keypart is complete for present keywords. What this means depend on the "
        desc_part2: str = "keyword, but f.x TITLE needs to have a value for all languages."

        self.val_result = ValidationResult(desc=desc_part1 + desc_part2)
        self.error_intro = ""
        self.model = model
        self.all_languages = model.languages.get_value()

        self.index_by_lang_and_variable = {}
        self.variables = {}
        for lang in self.all_languages:
            index = -1
            self.variables[lang] = self.model.stub.get_value(lang) + self.model.heading.get_value(lang)
            for variable in self.variables[lang]:
                index += 1
                self.index_by_lang_and_variable[(lang, variable)] = index

        # listOfOtherVariableNamesByVariableNameOfFirstLanguage

        self.indexByLangAndContentvalue = {}
        for lang in self.all_languages:
            index = -1
            contentvalues = self.model.values.get_value(self.model.contvariable.get_value(lang), lang)
            for contentvalue in contentvalues:
                index += 1
                self.indexByLangAndContentvalue[(lang, contentvalue)] = index

        for keyword_name in const.KEYWORDS_PYTHONIC_MAP:
            keyword = model.get_attribute(const.KEYWORDS_PYTHONIC_MAP[keyword_name])
            if keyword.is_present() and keyword.completeness_type:
                self.error_intro = f"For keyword {keyword._keyword}"

                if keyword.completeness_type == "Lang":
                    self.check_completeness_lang(keyword)
                elif keyword.completeness_type == "AllContent":
                    self.check_completeness_all_content(keyword)
                elif keyword.completeness_type == "EachVariable":
                    self.check_completeness_each_variable(keyword)
                elif keyword.completeness_type == "OneVariable":
                    self.check_completeness_one_variable(keyword)
                elif keyword.completeness_type == "AllVariables":
                    self.check_completeness_all_variables(keyword)
                elif keyword.completeness_type == "EachVarVal":
                    self.check_completeness_each_var_value(keyword)
                elif keyword.completeness_type == "X":
                    pass
                elif keyword.completeness_type == "TODO":
                    self.val_result.add_error(f"{self.error_intro}:Sorry keyword not supported yet.")
                else:  # pragma: no cover
                    raise Exception(f"{self.error_intro}:Sorry, unknown completeness_type:{keyword.completeness_type}")

    def check_completeness_lang(self, keyword: _PxValueByKey) -> None:
        for lang in self.all_languages:
            if not keyword.has_value(lang):
                self.val_result.add_error(f"{self.error_intro}:Missing value for lang:{lang}")

    def check_completeness_each_variable(self, keyword: _PxValueByKey) -> None:
        for key in keyword._value_by_key:
            all_tuples_same_variable_index = [
                k
                for k, v in self.index_by_lang_and_variable.items()
                if v == self.index_by_lang_and_variable[(key.lang, key.variable)]
            ]
            for one_tuple in all_tuples_same_variable_index:
                if key.lang == one_tuple[0]:
                    continue
                if not keyword.has_value(one_tuple[1], one_tuple[0]):
                    self.val_result.add_error(
                        f"{self.error_intro}:Missing value for variable:{one_tuple[1]} and lang:{one_tuple[0]}"
                    )

    def check_completeness_each_var_value(self, keyword: _PxValueByKey) -> None:
        for key in keyword._value_by_key:
            vari_pos = self.variables[key.lang].index(key.variable)
            value_pos = self.model.values.get_value(key.variable, key.lang).index(key.value)

            for lang in self.all_languages:
                if lang == key.lang:
                    continue

                vari_name = self.variables[lang][vari_pos]
                value_name = self.model.values.get_value(vari_name, lang)[value_pos]
                if not keyword.has_value(vari_name, value_name, lang):
                    self.val_result.add_error(
                        f"{self.error_intro}:Missing value for variable:{vari_name},value: {value_name} and lang:{lang}"
                    )

    def check_completeness_all_variables(self, keyword: _PxValueByKey) -> None:
        for lang in self.all_languages:
            for vari in self.variables[lang]:
                if not keyword.has_value(vari, lang):
                    self.val_result.add_error(f"{self.error_intro}:Missing value for variable:{vari} and lang:{lang}")

    def check_completeness_one_variable(self, keyword: _PxValueByKey) -> None:
        _seen_languages = {}
        the_one_index = ""
        for key in keyword._value_by_key:
            _seen_languages[key.lang] = 1
            tmp_index = self.index_by_lang_and_variable[(key.lang, key.variable)]
            if the_one_index == "":
                the_one_index = tmp_index
            else:
                if not tmp_index == the_one_index:
                    self.val_result.add_error(
                        f"{self.error_intro}: Should only reference 1 variable. Found 2: index {the_one_index} and {tmp_index}."
                    )

        for lang in self.all_languages:
            if lang not in _seen_languages:
                self.val_result.add_error(f"{self.error_intro}:Missing value for lang:{lang}")

    def check_completeness_all_content(self, keyword: _PxValueByKey) -> None:
        for lang in self.all_languages:
            for content in self.model.values.get_value(self.model.contvariable.get_value(lang), lang):
                if not keyword.has_value(content, lang):
                    self.val_result.add_error(f"{self.error_intro}:Missing value for content:{content} and lang:{lang}")


def check_completeness(model: PXFileModel) -> ValidationResult:
    return _Checker(model).val_result
