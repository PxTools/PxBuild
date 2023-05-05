from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.checks.check_lang_keys import check_lang_keys

import pytest



def test_check_lang():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en","fi"])
    pxfile.values.set(["v1", "v2"], "var", lang="sv")

    val_rep = check_lang_keys(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Specified language code \"sv\" for keyword VALUES must be one of the codes in keyword languages: \"no\",\"en\",\"fi\""