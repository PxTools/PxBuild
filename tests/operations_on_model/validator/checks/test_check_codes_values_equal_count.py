from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.checks.check_codes_values_equal_count import check_codes_values_equal_count

import pytest

def test_check_codes_values_equal_count_value_error():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_d", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_c", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_d", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="en")

    val_rep = check_codes_values_equal_count(pxfile)
    assert val_rep.is_valid == False 
    assert "The combination for language 'en' and variable 'var_d' in codes is not defined for any values." in val_rep.error_msg

def test_check_codes_values_equal_count_value_error_missing_key():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_d", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_c", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_d", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="en")

    val_rep = check_codes_values_equal_count(pxfile)
    assert val_rep.is_valid == False 
    assert "The combination for language 'en' and variable 'var_d' in codes is not defined for any values." in val_rep.error_msg
    
def test_check_codes_values_equal_count_value_error_missing_values():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="en")
    
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3", "v4"], variable="var_c", lang="en")

    val_rep = check_codes_values_equal_count(pxfile)
    assert val_rep.is_valid == False 
    assert "Codes and values does not have the same amout of entries for language 'en' and variable 'var_c'" in val_rep.error_msg