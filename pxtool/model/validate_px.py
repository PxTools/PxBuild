from pxtool.model.px_file_model import PXFileModel
import pxtool.model.util.constants as const
class ValidateMethods:

    def check_mandatory(model:PXFileModel) -> str:
        keyword_missing = []
        for key in const.MANDATORY_KEYWORDS:
            keyword = model.get_attribute(key)
            if not keyword.has_value():
                keyword_missing.append(keyword._keyword)
        
        if len(keyword_missing) > 0:
            error_msg_keywords = ", ".join(keyword_missing)
            raise ValueError(f"These kewywords are mandatory and is not set: {error_msg_keywords}")
           
        return "Mandatory keyword check complete.\n" 
    
    def check_language(model:PXFileModel) -> str:
        if (model.language.has_value() and model.languages.has_value()):
            if not model.language._px_value._string in model.languages._px_value.list_of_strings:
                raise ValueError(f"Specified language code \"{model.language._px_value._string}\" in keyword language must be one of the codes in keyword languages: {model.languages._px_value}")
        return "Language keyword check complete."

    def check_lang_keys(model:PXFileModel):
        if model.languages.has_value():
            for key in const.LANGDEPENDENT_KEYWORDS:
                keyword = model.get_attribute(key)
                if keyword.has_value():
                    for lang_key in keyword._value_by_key:
                        if not lang_key.lang in model.languages._px_value.list_of_strings:
                            raise ValueError(f"Specified language code \"{lang_key.lang}\" for keyword {keyword._keyword} must be one of the codes in keyword languages: {model.languages._px_value}")          
        
        return "All language keys are valid"    

    def check_decimals(model:PXFileModel) -> str:
        if not model.showdecimals.has_value():
            if model.decimals.get_value() > 6:
                raise ValueError(f"Value <{model.decimals.get_value()}> in decimals is not valid. When the keyword showdecimals is specified the value for decimals must be between 0 and 6.")
            
        return "Decimal check complete."
    
    def check_showdecimals(model:PXFileModel) -> str:
        if model.decimals.has_value() and model.showdecimals.has_value():
            if(model.showdecimals.get_value() > model.decimals.get_value()):
                raise ValueError(f"Value <{model.showdecimals.get_value()}> in showdecimals is not valid. The value must be less or equal decimals.")
            
        return "Showdecimal check complete."

    def check_codes_values_equal_count(model:PXFileModel) -> str:
        for key, value in model.codes._value_by_key.items():
            if not key in model.values._value_by_key.keys():
                raise ValueError(f"The combination {key.to_str_message()} in codes is not defined for any values.")
            if not len(value) == len(model.values._value_by_key[key]):
                    raise ValueError(f"Codes and values does not have the same amout of entries {key.to_str_message()}")
        return "Codes and values checked"


class ValidatePx:
    
    def is_valid(model:PXFileModel) -> bool:
        val_rep = [str]
        try:
            val_rep.append(ValidateMethods.check_mandatory(model))
            val_rep.append(ValidateMethods.check_codes_values_equal_count(model))
            val_rep.append(ValidateMethods.check_language(model))
            val_rep.append(ValidateMethods.check_decimals(model))
            val_rep.append(ValidateMethods.check_showdecimals(model))
            val_rep.append(ValidateMethods.check_lang_keys(model))
            print(*val_rep, sep='\n')
            return True
        except ValueError as e:
           print(f"Error: {e.args}")
           return False
        


 
        
    