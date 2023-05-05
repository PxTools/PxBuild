from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult

from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
from pxtool.operations_on_model.validator.checks.check_language import check_language
from pxtool.operations_on_model.validator.checks.check_lang_keys import check_lang_keys
from pxtool.operations_on_model.validator.checks.check_decimals import check_decimals
from pxtool.operations_on_model.validator.checks.check_showdecimals import check_showdecimals
from pxtool.operations_on_model.validator.checks.check_codes_values_equal_count import check_codes_values_equal_count

class Valdidate:
    runned_checks: list[ValidationResult]
    
    def __init__(self, model:PXFileModel):
        self.runned_checks = []
        self.passed = []
        self.failed = []
        try:
            self.runned_checks.append(check_mandatory(model))
            self.runned_checks.append(check_codes_values_equal_count(model))
            self.runned_checks.append(check_language(model))
            self.runned_checks.append(check_decimals(model))
            self.runned_checks.append(check_showdecimals(model))
            self.runned_checks.append(check_lang_keys(model))
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
        
    