from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_lang_keys import check_lang_keys

import pytest

def test_check_lang_keys_None_fails():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en","fi"])
    pxfile.subject_area.set("subject_area")
    
    val_rep = check_lang_keys(pxfile)
    assert val_rep.is_valid == False 
    assert "Specified language code \"None\" for keyword SUBJECT-AREA must be one of the codes in keyword languages: \"no\",\"en\",\"fi\"" in val_rep.error_msg

def test_check_lang_keys_unlisted_language_fails():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en","fi"])
    pxfile.values.set(["v1", "v2"], "var", lang="sv")

    val_rep = check_lang_keys(pxfile)
    assert val_rep.is_valid == False 
    assert "Specified language code \"sv\" for keyword VALUES must be one of the codes in keyword languages: \"no\",\"en\",\"fi\"" in val_rep.error_msg

