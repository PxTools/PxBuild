from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
import pxtool.model.util.constants as const

def check_language(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if default languge is defined in languages keyword")
        if not ( model.language.has_value() and model.languages.has_value()):
              val_result.add_error(f"Both keyword language and keyword languages must be present in model.")  
        elif not model.language.get_value() in model.languages.get_value():
           val_result.add_error(f"Specified language code \"{model.language._px_value._string}\" in keyword language must be one of the codes in keyword languages: {model.languages._px_value}")
        return val_result