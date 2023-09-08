from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.checks.check_values import check_values 

import pytest

def test_check_values_fails():
    pxfile = PXFileModel()
    pxfile.languages.set(["sv","fi"])

    pxfile.stub.set(["var1_sv","var2_sv"], "sv")
    pxfile.stub.set(["var1_fi","var2_fi"], "fi")

    pxfile.heading.set(["var3_sv"], "sv")
    pxfile.heading.set(["var3_fi"], "fi")

    val_rep = check_values(pxfile)
    assert val_rep.is_valid == False 
    assert "Can't find mandatory keyword VALUES." in val_rep.error_msg

    pxfile.values.set(["val1","val2"],"var1_sv","sv")
    val_rep = check_values(pxfile)
    assert val_rep.is_valid == False 
    assert "Can't find mandatory keyword VALUES for lang:fi and variable:var3_fi." in val_rep.error_msg
    
    pxfile.values.set(["val1","val2","val3"],"var2_sv","sv")
    pxfile.values.set(["val1"],"var3_sv","sv")
    pxfile.values.set(["val1","val2"],"var1_fi","fi")
    pxfile.values.set(["val1","val2","val3","val4"],"var2_fi","fi")
    pxfile.values.set(["val1"],"var3_fi","fi")
    val_rep = check_values(pxfile)
    assert val_rep.is_valid == False 
    assert "VALUES for lang:fi and variable:var2_fi. Found 4 entries, but another language had 3." in val_rep.error_msg


def test_check_values_ok():
    pxfile = PXFileModel()
    pxfile.languages.set(["sv","fi"])

    pxfile.stub.set(["var1_sv","var2_sv"], "sv")
    pxfile.stub.set(["var1_fi","var2_fi"], "fi")

    pxfile.heading.set(["var3_sv"], "sv")
    pxfile.heading.set(["var3_fi"], "fi")

    pxfile.values.set(["val1","val2"],"var1_sv","sv")
    pxfile.values.set(["val1","val2","val3","val4_sv"],"var2_sv","sv")
    pxfile.values.set(["val1"],"var3_sv","sv")
    pxfile.values.set(["val1","val2"],"var1_fi","fi")
    pxfile.values.set(["val1","val2","val3","val4"],"var2_fi","fi")
    pxfile.values.set(["val1"],"var3_fi","fi")
    val_rep = check_values(pxfile)
    assert val_rep.is_valid