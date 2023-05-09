from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
import pxtool.model.util.constants as const

def check_mandatory(model:PXFileModel) -> ValidationResult:
        val_result = ValidationResult(desc="Check if all mandatory keywords are set")
        keyword_missing = []
        for key in const.MANDATORY_KEYWORDS:
            keyword = model.get_attribute(key)
            if not keyword.is_present():
                keyword_missing.append(keyword._keyword)
        
        if len(keyword_missing) > 0:
            error_msg_keywords = ", ".join(keyword_missing)
            val_result.add_error(f"These kewywords are mandatory and is not set: {error_msg_keywords}")
        
        return val_result
    
 