from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from ...validator.validationResult import ValidationResult


def check_contentsvariable_is_present(model: PXFileModel) -> ValidationResult:
    val_result = ValidationResult(
        desc="Check that contentsvariable is present and placed in same position for all languages."
    )

    for langu in model.languages.get_value():
        try:
            cont_value = model.contvariable.get_value(langu)
        except:
            val_result.add_error(
                f"Value for Contentsvariable does not exist for for language code: {langu}. It must be specified."
            )
            return val_result

    first_pass = True
    for langu in model.languages.get_value():
        stub_and_head = model.stub.get_value(langu) + model.heading.get_value(langu)
        try:
            pos_contvariable = stub_and_head.index(model.contvariable.get_value(langu))
        except:
            val_result.add_error(
                f"Contentsvariable  not found in stub or heading for language code: {langu}.  It must exist in either stub or heading."
            )
            return val_result
        if first_pass:
            first_langu = langu
            first_pass = False
            pos_contvariable_first = pos_contvariable
        else:
            if pos_contvariable != pos_contvariable_first:
                val_result.add_error(
                    f"Position of contentsvariable does not matchs in HEADING or STUB for language code: {langu} and {first_langu}."
                )
    return val_result
