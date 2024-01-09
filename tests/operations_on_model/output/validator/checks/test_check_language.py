from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_language import check_language

import pytest

def test_check_language_ok():
    model = PXFileModel()
    model.languages.set(["no","en","fi"])
    model.language.set("no")

    val_rep = check_language(model)
    assert val_rep.is_valid == True

def test_check_language_missing():
    model = PXFileModel()
    val_rep = check_language(model)
    assert val_rep.is_valid == False
    assert "Both keyword language and keyword languages must be present in model." in val_rep.error_msg

def test_check_language_bad_lang():
    model = PXFileModel()
    model.languages.set(["no","en","fi"])
    model.language.set("sv")

    val_rep = check_language(model)
    assert val_rep.is_valid == False 
    assert "Specified language code \"sv\" in keyword language must be one of the codes in keyword languages: \"no\",\"en\",\"fi\"" in val_rep.error_msg
