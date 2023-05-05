from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
import pxtool.model.util.constants as const

   
def check_showdecimals(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if value for showdecimals is greater than value for decimals")
        if model.decimals.has_value() and model.showdecimals.has_value():
            if(model.showdecimals.get_value() > model.decimals.get_value()):
                val_result.add_error(f"Value <{model.showdecimals.get_value()}> in showdecimals is not valid. The value must be less or equal decimals.")
        return val_result