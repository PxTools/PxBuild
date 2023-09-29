from pxtool.models.output.pxfile.px_file_model import PXFileModel
from pxtool.operations_on_model.output.validator.checks.check_contentsvariable_is_present import check_contentsvariable_is_present
import pytest

def test_contentsvariable_is_ok_both_languages_lang():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en"])
    pxfile.contvariable.set("statvar","no")
    pxfile.contvariable.set("contents","en")
    pxfile.stub.set(["var_no_1","var_no_2","var_no_3"], "no")
    pxfile.stub.set(["var_en_1","var_en_2","var_en_3"], "en") 
    pxfile.heading.set(["var_no_4","statvar","var_no_5"], "no")
    pxfile.heading.set(["var_en_4","contents","var_en_5"], "en") 
    val_rep = check_contentsvariable_is_present(pxfile)
    assert val_rep.is_valid == True
    
def test_contentsvariable_is_missing_first_lang():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en"])
    pxfile.contvariable.set("contents","en")
    pxfile.stub.set(["var_no_1","var_no_2","var_no_3"], "no")
    pxfile.stub.set(["var_en_1","var_en_2","var_en_3"], "en") 
    pxfile.heading.set(["var_no_4","statvar","var_no_5"], "no")
    pxfile.heading.set(["var_en_4","contents","var_en_5"], "en") 
    val_rep = check_contentsvariable_is_present(pxfile)
    assert val_rep.is_valid == False
    assert val_rep.error_msg == "Value for Contentsvariable does not exist for for language code: no. It must be specified."
    
def test_contentsvariable_is_missing_second_lang():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en"])
    pxfile.contvariable.set("statvar","no")
    pxfile.stub.set(["var_no_1","var_no_2","var_no_3"], "no")
    pxfile.stub.set(["var_en_1","var_en_2","var_en_3"], "en") 
    pxfile.heading.set(["var_no_4","statvar","var_no_5"], "no")
    pxfile.heading.set(["var_en_4","contents","var_en_5"], "en") 
    val_rep = check_contentsvariable_is_present(pxfile)
    assert val_rep.is_valid == False
    assert val_rep.error_msg == "Value for Contentsvariable does not exist for for language code: en. It must be specified."

def test_contentsvariable_position_doent_match():
    pxfile = PXFileModel()
    pxfile.languages.set(["no","en"])
    pxfile.contvariable.set("statvar","no")
    pxfile.contvariable.set("contents","en")
    pxfile.stub.set(["var_no_1","var_no_2","var_no_3"], "no")
    pxfile.stub.set(["var_en_1","var_en_2","var_en_3"], "en") 
    pxfile.heading.set(["statvar","var_no_4","var_no_5"], "no")
    pxfile.heading.set(["var_en_4","contents","var_en_5"], "en") 
    val_rep = check_contentsvariable_is_present(pxfile)
    assert val_rep.is_valid == False
    assert val_rep.error_msg == "Position of contentsvariable does not matchs in HEADING or STUB for language code: en and no."