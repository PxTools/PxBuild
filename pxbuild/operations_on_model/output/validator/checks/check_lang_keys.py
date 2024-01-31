from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult
import pxbuild.models.output.pxfile.util.constants as const
from .check_mandatory import check_mandatory


def check_lang_keys(model: PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check if all language keys have a valid language")
    for key in const.LANGDEPENDENT_KEYWORDS:
        keyword = model.get_attribute(key)
        if keyword.is_present():
            for lang_key in keyword._value_by_key:
                if not lang_key.lang in model.languages.get_value():
                    val_result.add_error(
                        f'Specified language code "{lang_key.lang}" for keyword {keyword._keyword} must be one of the codes in keyword languages: {model.languages._px_value}'
                    )
    return val_result
