from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult


def check_decimals(model: PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check if value for decimals has is lower than 6 if showdecimals is not defined")
    if not model.showdecimals.has_value():
        if model.decimals.get_value() > 6:
            mess_part1: str = f"Value <{model.decimals.get_value()}> in decimals is not valid. When the keyword "
            mess_part2: str = "showdecimals is not specified, the value for decimals must be between 0 and 6."
            val_result.add_error(mess_part1 + mess_part2)
    return val_result
