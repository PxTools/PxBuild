from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult

from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
from pxtool.operations_on_model.validator.checks.check_language import check_language
from pxtool.operations_on_model.validator.checks.check_lang_keys import check_lang_keys
from pxtool.operations_on_model.validator.checks.check_decimals import check_decimals
from pxtool.operations_on_model.validator.checks.check_showdecimals import check_showdecimals
from pxtool.operations_on_model.validator.checks.check_codes_values_equal_count import check_codes_values_equal_count
from pxtool.operations_on_model.validator.checks.check_stub_and_heading import check_stub_and_heading
from pxtool.operations_on_model.validator.checks.check_contentsvariable_is_present import check_contentsvariable_is_present
from pxtool.operations_on_model.validator.checks.check_values import check_values
from pxtool.operations_on_model.validator.checks.check_subkeys import check_valuebased_subkeys
from pxtool.operations_on_model.validator.checks.check_completeness import check_completeness

class Valdidate:
    checks_ran: list[ValidationResult]
    
    def __init__(self, model:PXFileModel):
        self.checks_ran = []
        self.passed = []
        self.failed = []

        self.run_checks(model)
        
        
        for rep in self.checks_ran:
            if rep.is_valid:
                self.passed.append(rep)
            else:
                self.failed.append(rep)

    def run_checks(self, model:PXFileModel) -> None:

        self.checks_ran.append(check_language(model))
        if not self.checks_ran[-1].is_valid:
            return     
        
        self.checks_ran.append(check_stub_and_heading(model))
        if not self.checks_ran[-1].is_valid:
            return   
        
        self.checks_ran.append(check_contentsvariable_is_present(model))
        if not self.checks_ran[-1].is_valid:
            return              
        
        self.checks_ran.append(check_values(model))
        if not self.checks_ran[-1].is_valid:
            return  
        
        self.checks_ran.append(check_lang_keys(model))
        if not self.checks_ran[-1].is_valid:
            return
                 
        self.checks_ran.append(check_valuebased_subkeys(model))
        if not self.checks_ran[-1].is_valid:
            return    
                 
        self.checks_ran.append(check_mandatory(model))
        if not self.checks_ran[-1].is_valid:
            return 
        
        self.checks_ran.append(check_completeness(model))
        if not self.checks_ran[-1].is_valid:
          return        
        #
        self.checks_ran.append(check_codes_values_equal_count(model))
        self.checks_ran.append(check_decimals(model))
        self.checks_ran.append(check_showdecimals(model))

    def is_valid(self) -> bool:
        return (not len(self.failed) > 0)

    def get_report(self) -> str:
        my_out = "Validation report: \n"
        my_out += f"Total checks done: {len(self.checks_ran)} \n"
        my_out += f"Passed: {len(self.passed)} \n"
        for rep in self.passed:
            my_out += str(rep) + "\n"
        
        my_out += "\n" +self.get_errors()

        return my_out
       

    def get_errors(self) -> str:
        if self.is_valid():
            return "Validated without errors. No errors to print."
        else:
            my_out = f"Failed: {len(self.failed )}\n"
            for rep in self.failed:
                my_out +=  str(rep) + "\n"
            return my_out
        
    