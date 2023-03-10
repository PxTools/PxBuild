from pxtool.model.px_file_model import PXFileModel
from pxtool.model.validate_px import Validator as val
import pytest


def test_check_decimals_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(7)

    val_rep = val.check_decimals(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Value <7> in decimals is not valid. When the keyword showdecimals is specified the value for decimals must be between 0 and 6."

def test_check_decimals_is_valid():
    pxfile = PXFileModel()
    pxfile.decimals.set(5)

    val_rep = val.check_decimals(pxfile)
    assert val_rep.is_valid == True 

def test_check_showdecimals_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(2)
    pxfile.showdecimals.set(3)
    
    val_rep = val.check_showdecimals(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Value <3> in showdecimals is not valid. The value must be less or equal decimals."

def test_check_codes_values_equal_count_value_error():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_d", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_c", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_d", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="en")

    val_rep = val.check_codes_values_equal_count(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "The combination for language 'en' and variable 'var_d' in codes is not defined for any values."

def test_check_codes_values_equal_count_value_error_missing_key():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_d", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_c", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_d", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="en")

    val_rep = val.check_codes_values_equal_count(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "The combination for language 'en' and variable 'var_d' in codes is not defined for any values."
    
def test_check_codes_values_equal_count_value_error_missing_values():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="en")
    
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3", "v4"], variable="var_c", lang="en")

    val_rep = val.check_codes_values_equal_count(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Codes and values does not have the same amout of entries for language 'en' and variable 'var_c'"

def test_check_mandatory_returns_error():
    pxfile = PXFileModel()
    pxfile.title.set(title="TableTitle", lang="no")
    pxfile.decimals.set(2)
    pxfile.matrix.set(matrix="TestMatrix")

    val_rep = val.check_mandatory(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "These kewywords are mandatory and is not set: SUBJECT-CODE, SUBJECT-AREA, DESCRIPTION, CONTENTS, UNITS, STUB, HEADING, VALUES, ATTRIBUTE-ID, ATTRIBUTE-TEXT, ATTRIBUTES, DATA"

def test_check_lang():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en","fi"])
    pxfile.values.set(["v1", "v2"], "var", lang="sv")

    val_rep = val.check_lang_keys(pxfile)
    assert val_rep.is_valid == False 
    assert val_rep.error_msg == "Specified language code \"sv\" for keyword VALUES must be one of the codes in keyword languages: \"no\",\"en\",\"fi\""




