from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult
import pxbuild.models.output.pxfile.util.constants as const

def check_stub_and_heading(model:PXFileModel) -> ValidationResult:
    val_result = ValidationResult(desc="Check if both stub and heading has the same len for each language.")

    first_pass = True 

    for langu in model.languages.get_value():
        if not (model.stub.has_value(langu) or model.heading.has_value(langu) ) :
           val_result.add_error(f"For language code \"{langu}\": Neither STUB nor HEADING found.")
           continue

        if first_pass:
            first_pass = False
            first_langu = langu
            if model.stub.has_value(langu):
                stub_length = len(model.stub.get_value(langu))
            else:
                stub_length = -1

            if model.heading.has_value(langu):
                heading_length = len(model.heading.get_value(langu))
            else:
                heading_length = -1 
        else:
            if model.stub.has_value(langu):
                cur_stub_length = len(model.stub.get_value(langu))
            else:
                cur_stub_length = -1
            if not cur_stub_length == stub_length:
               val_result.add_error(f"Number of items in STUB don't match when comparing language code: {langu} and {first_langu}.")

            if model.heading.has_value(langu):
                cur_heading_length = len(model.heading.get_value(langu))
            else:
                cur_heading_length = -1
            if not cur_heading_length == heading_length:
               val_result.add_error(f"Number of items in HEADING don't match when comparing language code: {langu} and {first_langu}.")

    return val_result