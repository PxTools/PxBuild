from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult


def check_showdecimals(model: PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check if value for showdecimals is greater than value for decimals")
    if model.showdecimals.has_value():
        if model.showdecimals.get_value() > model.decimals.get_value():
            val_result.add_error(
                f"Value <{model.showdecimals.get_value()}> in showdecimals is not valid. The value must be less or equal decimals."
            )
    return val_result
