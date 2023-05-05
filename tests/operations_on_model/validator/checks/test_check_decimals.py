from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.checks.check_decimals import check_decimals 

import pytest

def test_check_decimals_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(7)

    val_rep = check_decimals(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Value <7> in decimals is not valid. When the keyword showdecimals is specified the value for decimals must be between 0 and 6."

def test_check_decimals_is_valid():
    pxfile = PXFileModel()
    pxfile.decimals.set(5)

    val_rep = check_decimals(pxfile)
    assert val_rep.is_valid == True 