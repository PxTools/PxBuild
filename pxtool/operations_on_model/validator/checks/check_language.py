from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
from pxtool.operations_on_model.validator.checks.check_mandatory import  check_mandatory
import pxtool.model.util.constants as const

def check_language(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if default languges is defined in languages keyword")
        if (model.language.has_value() and model.languages.has_value()):
            if not model.language._px_value._string in model.languages._px_value.list_of_strings:
                val_result.add_error(f"Specified language code \"{model.language._px_value._string}\" in keyword language must be one of the codes in keyword languages: {model.languages._px_value}")
        return val_result