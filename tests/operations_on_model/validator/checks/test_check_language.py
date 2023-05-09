from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.checks.check_language import check_language

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
    assert "Both keyword language and keyword languages must be present in model." == val_rep.error_msg

def test_check_language_bad_lang():
    model = PXFileModel()
    model.languages.set(["no","en","fi"])
    model.language.set("sv")

    val_rep = check_language(model)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Specified language code \"sv\" in keyword language must be one of the codes in keyword languages: \"no\",\"en\",\"fi\""
