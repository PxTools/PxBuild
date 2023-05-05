from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult

from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory


import pxtool.model.util.constants as const

class Validator:
    def check_language(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if default languges is defined in languages keyword")
        if (model.language.has_value() and model.languages.has_value()):
            if not model.language._px_value._string in model.languages._px_value.list_of_strings:
                val_result.add_error(f"Specified language code \"{model.language._px_value._string}\" in keyword language must be one of the codes in keyword languages: {model.languages._px_value}")
        return val_result

    def check_lang_keys(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if all language keys have a valid language")
        if model.languages.has_value():
            for key in const.LANGDEPENDENT_KEYWORDS:
                keyword = model.get_attribute(key)
                if keyword.has_value():
                    for lang_key in keyword._value_by_key:
                        if not lang_key.lang in model.languages._px_value.list_of_strings:
                            val_result.add_error(f"Specified language code \"{lang_key.lang}\" for keyword {keyword._keyword} must be one of the codes in keyword languages: {model.languages._px_value}")
        return val_result

    def check_decimals(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if value for decimals has is lower than 6 if showdecimals is defined")
        if not model.showdecimals.has_value():
            if model.decimals.get_value() > 6:
                val_result.add_error(f"Value <{model.decimals.get_value()}> in decimals is not valid. When the keyword showdecimals is specified the value for decimals must be between 0 and 6.")
        return val_result
    
    def check_showdecimals(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if value for showdecimals is greater than value for decimals")
        if model.decimals.has_value() and model.showdecimals.has_value():
            if(model.showdecimals.get_value() > model.decimals.get_value()):
                val_result.add_error(f"Value <{model.showdecimals.get_value()}> in showdecimals is not valid. The value must be less or equal decimals.")
        return val_result
    
    def check_codes_values_equal_count(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if language and variable are defined for both codes and values and that they have the same amount of values.")
        for key, value in model.codes._value_by_key.items():
            if not key in model.values._value_by_key.keys():
                val_result.add_error(error=f"The combination {key.to_str_message()} in codes is not defined for any values.")
                return val_result
            if not len(value) == len(model.values._value_by_key[key]):
                    val_result.add_error(error=f"Codes and values does not have the same amout of entries {key.to_str_message()}")
        return val_result

class Valdidate:
    runned_checks: list[ValidationResult]
    
    def __init__(self, model:PXFileModel):
        self.runned_checks = []
        self.passed = []
        self.failed = []
        try:
            self.runned_checks.append(check_mandatory(model))
            self.runned_checks.append(Validator.check_codes_values_equal_count(model))
            self.runned_checks.append(Validator.check_language(model))
            self.runned_checks.append(Validator.check_decimals(model))
            self.runned_checks.append(Validator.check_showdecimals(model))
            self.runned_checks.append(Validator.check_lang_keys(model))
        except Exception as e:
            print(f"Error: {e.args}")
        
        for rep in self.runned_checks:
            if rep.is_valid:
                self.passed.append(rep)
            else:
                self.failed.append(rep)

    def is_valid(self) -> bool:
        return (not len(self.failed) > 0)

    def print_report(self):
        print("Validation report: \n")
        print(f"Total checks done: {len(self.runned_checks)} \n")
        print(f"Passed: {len(self.passed)} \n")
        for rep in self.passed:
            print(str(rep), "\n")
        
        print(f"Failed: {len(self.failed )}\n")
        for rep in self.failed:
            print(str(rep), "\n")
       

    def print_errors(self):
        if self.is_valid():
            print("Validated without errors. No errors to print.")
        else:                
            print(f"Failed: {len(self.failed )}\n")
            for rep in self.failed:
                print(str(rep), "\n")
        
    