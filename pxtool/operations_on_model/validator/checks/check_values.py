from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
import pxtool.model.util.constants as const

def check_values(model:PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check if all combination of language and variables has a value-list. And that a variable has the same number of values in all langs.")
    if not model.values.is_present():
        val_result.add_error(f"Can't find mandatory keyword VALUES.")
        return val_result
    
    lengths_by_variable = {}

    for langu in model.languages.get_value():
        variables = model.stub.get_value(langu) + model.heading.get_value(langu)
        vari_cnt=0
        for vari in variables:
            vari_cnt += 1
            if not model.values.has_value(vari, langu):
                val_result.add_error(f"Can't find mandatory keyword VALUES for lang:{langu} and variable:{vari}.")
            else:
                curr_len = len(model.values.get_value(vari, langu))
                if vari_cnt in lengths_by_variable:
                    if not curr_len == lengths_by_variable[vari_cnt]:
                        val_result.add_error(f"VALUES for lang:{langu} and variable:{vari}. Found {curr_len} entries, but another language had {lengths_by_variable[vari_cnt]}. ")
                else:
                    lengths_by_variable[vari_cnt] = curr_len        
    return val_result
