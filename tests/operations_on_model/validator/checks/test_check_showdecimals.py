from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.checks.check_showdecimals import check_showdecimals

import pytest

def test_check_showdecimals_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(2)
    pxfile.showdecimals.set(3)
    
    val_rep = check_showdecimals(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Value <3> in showdecimals is not valid. The value must be less or equal decimals."