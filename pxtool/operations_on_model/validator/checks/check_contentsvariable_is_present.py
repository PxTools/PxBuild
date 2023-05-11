from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validationResult import ValidationResult
import pxtool.model.util.constants as const

def check_contentsvariable_is_present(model:PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check that contentsvariable is present and placed in same position for all languages.")

    if len(model.contvariable) < 1 :
        val_result.add_error(f"Contentsvariable does not exist. It must be specified.")
        return  val_result   
    cont_variable_name = model.contvariable
    first_pass = True 
    

    for langu in model.languages.get_value():
        stub_and_head = model.stub.get_value(langu) +  model.heading.get_value(langu) 
        try:
            pos_contvariable = stub_and_head.index(model.contvariable.get_value(langu))  
        except:
            val_result.add_error(f"Contentsvariable  not found in stub or heading for language code: {langu}.  It must exist in either stub or heading.")
            return val_result
        if first_pass:
            first_langu = langu
            first_pass = False
            pos_contvariable_first = pos_contvariable 
        else:
            if  pos_contvariable != pos_contvariable_first:
               val_result.add_error(f"Position of contentsvariable does not matchs in HEADING or STUB for language code: {langu} and {first_langu}.")
    return val_result