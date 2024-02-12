from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult


def check_language(model: PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check if default languge is defined in languages keyword")
    if not (model.language.has_value() and model.languages.has_value()):
        val_result.add_error(f"Both keyword language and keyword languages must be present in model.")
    elif model.language.get_value() not in model.languages.get_value():
        mess_part1: str = f'Specified language code "{model.language._px_value._string}" in keyword language '
        mess_part2: str = f"must be one of the codes in keyword languages: {model.languages._px_value}"
        val_result.add_error(mess_part1 + mess_part2)
    return val_result
