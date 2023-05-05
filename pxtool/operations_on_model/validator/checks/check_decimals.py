from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
import pxtool.model.util.constants as const

def check_decimals(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if value for decimals has is lower than 6 if showdecimals is not defined")
        if not model.showdecimals.has_value():
            if model.decimals.get_value() > 6:
                val_result.add_error(f"Value <{model.decimals.get_value()}> in decimals is not valid. When the keyword showdecimals is not specified, the value for decimals must be between 0 and 6.")
        return val_result