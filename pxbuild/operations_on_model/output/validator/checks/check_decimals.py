from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult
import pxbuild.models.output.pxfile.util.constants as const

from .check_mandatory import  check_mandatory

def check_decimals(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if value for decimals has is lower than 6 if showdecimals is not defined")
        if not model.showdecimals.has_value():
            if model.decimals.get_value() > 6:
                val_result.add_error(f"Value <{model.decimals.get_value()}> in decimals is not valid. When the keyword showdecimals is not specified, the value for decimals must be between 0 and 6.")
        return val_result