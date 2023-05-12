from pxtool.model.px_file_model import PXFileModel
from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_keytypes import _KeytypeVariableLang, _KeytypeContentLang, _KeytypeVariableValueLang, _KeytypeValuesLangMulti, _KeytypeCodes

from pxtool.operations_on_model.validator.validationResult import ValidationResult
import pxtool.model.util.constants as const

class _Checker:
    def __init__(self, model:PXFileModel) -> None:
        self.val_result = ValidationResult(desc="Check if the keypart is complete for present keywords. What this means depend on the keyword, but f.x TITLE needs to have a value for all languages. ")
        self.error_intro = ""
        self.model = model
        self.all_languages = model.languages.get_value()

        self.indexByLangAndVariable = {}
        for lang in self.all_languages:
                index=-1
                variables = self.model.stub.get_value(lang) + self.model.heading.get_value(lang)            
                for variable in variables:
                    index += 1
                    self.indexByLangAndVariable[(lang,variable)] = index

        
        #listOfOtherVariableNamesByVariableNameOfFirstLanguage


        self.indexByLangAndContentvalue = {}
        for lang in self.all_languages:
                index=-1
                contentvalues = self.model.values.get_value(self.model.contvariable.get_value(lang),lang)            
                for contentvalue in contentvalues:
                    index += 1
                    self.indexByLangAndContentvalue[(lang,contentvalue)] = index

        for keyword_name in const.KEYWORDS_PYTHONIC_MAP:
            keyword = model.get_attribute(const.KEYWORDS_PYTHONIC_MAP[keyword_name])
            if keyword.is_present() and keyword.completeness:
                self.error_intro = f"For keyword {keyword._keyword}"
                if keyword.completeness == "Lang":
                    self.check_completeness_lang(keyword)



    def check_completeness_lang(self, keyword:_PxValueByKey) -> None:
        for lang in self.all_languages:
            if not keyword.has_value(lang):
                self.val_result.add_error(f"{self.error_intro}:Missing value for lang:{lang}")


    def check_keytype_lang_with_subkey(self, keyword:_PxValueByKey) -> None:
        
        for key in keyword._value_by_key:
            for lang in self.all_languages:
                if not lang == key.lang:
                   if not keyword.has_value():
                       pass  




    def check_keytype_values(self, key:_KeytypeValuesLangMulti, keyword:_PxValueByKey) -> None:  
        if not key.values:
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Values can not be None. For lang:{key.lang}.")
        else:
            dimensions = self.model.stub.get_value(key.lang) + self.model.heading.get_value(key.lang)
            if not len(dimensions) == len(key.values):
                   self.val_result.add_error(f"{self.error_intro}: There are {len(dimensions)} dimensions, but {len(key.values)} values. For lang:{key.lang}.")
            else:
                dimension_cnt=-1
                for value in key.values:
                    dimension_cnt += 1
                    if value == "*":
                        continue
                    self.check_if_value_in_values(key.lang,dimensions[dimension_cnt],value,self.model)




    def check_keytype_variable(self, key:_KeytypeVariableLang, keyword:_PxValueByKey) -> None:                           
        if not key.variable:
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Variable can not be None. For lang:{key.lang}.")
        else:
            self.check_variable_in_stub_or_heading(key.lang, key.variable, self.model)

    def check_keytype_variable_value(self, key:_KeytypeVariableValueLang, keyword:_PxValueByKey) -> None:   
        if not key.variable:
            if key.value:
                self.val_result.add_error(f"{self.error_intro}: Found value, but no variable . For lang:{key.lang}.")
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Variable can not be None. For lang:{key.lang}.")
        else:
            if not key.value:
                if not keyword.subkey_optional:
                    self.val_result.add_error(f"{self.error_intro}: Need value for variable {key.variable}. For lang:{key.lang}.")        
            else:
                if self.check_variable_in_stub_or_heading(key.lang, key.variable, self.model):
                    self.check_if_value_in_values(key.lang, key.variable, key.value, self.model)   


    def check_keytype_content(self, key:_KeytypeContentLang, keyword:_PxValueByKey) -> None:                        
        if not key.content:
            if not keyword.subkey_optional:
                self.val_result.add_error(f"{self.error_intro}: Content value can not be None. For lang:{key.lang}.")
        else:
            self.check_if_value_in_values(key.lang, self.model.contvariable.get_value(key.lang), key.content, self.model)                                       
                                      

    def check_if_value_in_values(self, lang:str, dimension:str, value:str, model:PXFileModel) -> bool:
        my_out = value in model.values.get_value(dimension,lang)
        if not my_out :
            self.val_result.add_error(f"{self.error_intro}: Cannot find item {value} in VALUES for vaiable:{dimension} and lang:{lang}.")
        return my_out

    def check_variable_in_stub_or_heading(self, lang:str, variable:str, model:PXFileModel) -> bool:
        my_out = variable in model.stub.get_value(lang) + model.heading.get_value(lang)
        if not my_out :
            self.val_result.add_error(f"{self.error_intro}: Cannot find variable {variable} in stub + heading. For lang:{lang}.")
        return my_out


def check_completeness(model:PXFileModel) -> ValidationResult:
    return _Checker(model).val_result