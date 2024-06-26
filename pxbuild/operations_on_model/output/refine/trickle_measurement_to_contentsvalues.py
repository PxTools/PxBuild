import pxbuild.models.output.pxfile.util.constants as constants
from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeContentLang


from pxbuild.operations_on_model.output.validator.checks.check_contentsvariable_is_present import (
    check_contentsvariable_is_present,
)
from pxbuild.operations_on_model.output.validator.checks.check_lang_keys import check_lang_keys
from pxbuild.operations_on_model.output.validator.checks.check_language import check_language
from pxbuild.operations_on_model.output.validator.checks.check_stub_and_heading import (
    check_stub_and_heading,
)
from pxbuild.operations_on_model.output.validator.checks.check_values import check_values


def trickle_measurement_to_contentsvalues(model: PXFileModel):
    """if model has CONTVARIABLE and UNITS are without contvalue , insert one for each value
    So that
    CONTVARIABLE[en]="My contents var"
    VALUES[en]("My contents var")="Val1",Val2"
    UNITS[en]= "NOK"
    DAYADJ[en]= TRUE
    DAYADJ[en]("Val2")= FALSE
    SEASADJ[en]("Val2")= TRUE
    ==>
    UNITS[en]("Val1")= "NOK"
    DAYADJ[en]("Val1")= TRUE
    UNITS[en]("Val2")= "NOK"
    DAYADJ[en]("Val2")= FALSE
    SEASADJ[en]("Val2")= TRUE
    """

    if (
        not check_language(model).is_valid
        or not check_stub_and_heading(model).is_valid
        or not check_contentsvariable_is_present(model).is_valid
        or not check_values(model).is_valid
        or not check_lang_keys(model).is_valid
    ):
        # TODO better err mess
        raise Exception(
            "One of check_language, check_stub_and_heading, check_contentsvariable_is_present, check_values or check_lang_keys is not valid."
        )

    content_indexed_keywords = constants.CONTENT_INDEXED_KEYWORDS

    for keyword_name in content_indexed_keywords:
        keyword = model.get_attribute(keyword_name)
        if not keyword.is_present():
            continue

        for lang in model.languages.get_value():
            if not keyword.has_value(None, lang):
                continue
            the_value = keyword._value_by_key.pop(_KeytypeContentLang(None, lang))
            for conti in model.values.get_value(model.contvariable.get_value(lang), lang):
                if keyword.has_value(conti, lang):
                    continue

                new_key = _KeytypeContentLang(None, lang)
                keyword._value_by_key[new_key] = the_value
