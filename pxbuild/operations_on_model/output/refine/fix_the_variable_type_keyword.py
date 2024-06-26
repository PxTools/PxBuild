from pxbuild.models.output.pxfile.px_file_model import PXFileModel

from pxbuild.operations_on_model.output.validator.checks.check_contentsvariable_is_present import (
    check_contentsvariable_is_present,
)
from pxbuild.operations_on_model.output.validator.checks.check_lang_keys import check_lang_keys
from pxbuild.operations_on_model.output.validator.checks.check_language import check_language
from pxbuild.operations_on_model.output.validator.checks.check_stub_and_heading import (
    check_stub_and_heading,
)
from pxbuild.operations_on_model.output.validator.checks.check_subkeys import (
    check_valuebased_subkeys,
)
from pxbuild.operations_on_model.output.validator.checks.check_values import check_values


def fix_the_variable_type_keyword(model: PXFileModel):
    """
    Makes sure there is a VARIABLE-TYPE for each variable and language:
    Will not overwrite existing. Using
    T for time
    C for content
    G for geo
    N for Normal
    """

    if (
        not check_language(model).is_valid
        or not check_stub_and_heading(model).is_valid
        or not check_contentsvariable_is_present(model).is_valid
        or not check_values(model).is_valid
        or not check_lang_keys(model).is_valid
        or not check_valuebased_subkeys(model).is_valid
    ):
        # TODO better err mess
        raise ValueError(
            "One of check_language, check_stub_and_heading, check_contentsvariable_is_present, check_values,"
            + " check_lang_keys or  check_valuebased_subkeys is not valid."
        )

    for lang in model.languages.get_value():
        for vari in model.stub.get_value(lang) + model.heading.get_value(lang):
            if model.variable_type.has_value(vari, lang):
                continue

            if model.timeval.has_value(vari, lang):
                model.variable_type.set("T", vari, lang)
            elif model.contvariable.get_value(lang) == vari:
                model.variable_type.set("C", vari, lang)
            elif model.map.has_value(vari, lang):
                model.variable_type.set("G", vari, lang)
            else:
                model.variable_type.set("N", vari, lang)
