from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
import pxtool.model.util.constants as const

def check_codes_values_equal_count(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if language and variable are defined for both codes and values and that they have the same amount of values.")
        for key, value in model.codes._value_by_key.items():
            if not key in model.values._value_by_key.keys():
                val_result.add_error(error=f"The combination {key.to_str_message()} in codes is not defined for any values.")
                return val_result
            if not len(value) == len(model.values._value_by_key[key]):
                    val_result.add_error(error=f"Codes and values does not have the same amout of entries {key.to_str_message()}")
        return val_result