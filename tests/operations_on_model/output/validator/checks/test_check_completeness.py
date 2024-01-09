from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_completeness import check_completeness

import pytest

def _get_model() -> PXFileModel:
    pxfile = PXFileModel()
    pxfile.languages.set(["sv","fi"])

    pxfile.stub.set(["var1_sv","var2_sv"], "sv")
    pxfile.stub.set(["var1_fi","var2_fi"], "fi")

    pxfile.heading.set(["var3_sv"], "sv")
    pxfile.heading.set(["var3_fi"], "fi")

    pxfile.values.set(["v_1_1_sv","v_1_2_sv"],"var1_sv","sv")
    pxfile.values.set(["v_2_1_sv","v_2_2_sv"],"var2_sv","sv")
    pxfile.values.set(["v_3_1_sv","v_3_2_sv"],"var3_sv","sv")
    
    pxfile.values.set(["v_1_1_fi","v_1_2_fi"],"var1_fi","fi")
    pxfile.values.set(["v_2_1_fi","v_2_2_fi"],"var2_fi","fi")
    pxfile.values.set(["v_3_1_fi","v_3_2_fi"],"var3_fi","fi")
    
    pxfile.contvariable.set("var2_sv","sv")
    pxfile.contvariable.set("var2_fi","fi")
    pxfile.units.set("Units for v_2_1_sv","v_2_1_sv","sv")
    pxfile.units.set("Units for v_2_1_fi","v_2_1_fi","fi")
    pxfile.units.set("Units for v_2_2_sv","v_2_2_sv","sv")
    pxfile.units.set("Units for v_2_2_fi","v_2_2_fi","fi")    
    pxfile.seasadj.set(True,"v_2_1_sv","sv")
    pxfile.seasadj.set(True,"v_2_1_fi","fi")
    pxfile.seasadj.set(True,"v_2_2_sv","sv")
    pxfile.seasadj.set(True,"v_2_2_fi","fi")

    pxfile.note.set("A note for table in sv", None, "sv")
    pxfile.note.set("A note for table in fi", None, "fi")

    pxfile.precision.set(2, "var1_sv", "v_1_1_sv", "sv")
    pxfile.precision.set(2, "var1_fi", "v_1_1_fi", "fi")   

    pxfile.cellnote.set("A cellnote",["v_1_1_sv","v_2_1_sv","*"],"sv")
    pxfile.cellnote.set("A cellnote",["v_1_1_fi","v_2_1_fi","*"],"fi")

   
    return pxfile

#Timeval is (currently ) the only Keyword with One_variable
def test_check_completeness_one_variable_fails_keyword_not_supported():
    pxfile = _get_model()
    pxfile.attributes.set(["C","F"],["C1","C2","C3"])

    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword ATTRIBUTES:Sorry keyword not supported yet." in val_rep.error_msg

#Timeval is (currently ) the only Keyword with One_variable
def test_check_completeness_one_variable_fails_half_a_variable():
    pxfile = _get_model()
    pxfile.timeval.set("A1",["T1","T2"],"var1_sv","sv")

    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword TIMEVAL:Missing value for lang:fi" in val_rep.error_msg

def test_check_completeness_one_variable_ok_one_variable():
    pxfile = _get_model()
    pxfile.timeval.set("A1",["T1","T2"],"var1_sv","sv")
    pxfile.timeval.set("A1",["T1","T2"],"var1_fi","fi")
    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid 

def test_check_completeness_one_variable_fails_2_variables():
    pxfile = _get_model()
    pxfile.timeval.set("A1",["T1","T2"],"var1_sv","sv")
    pxfile.timeval.set("A1",["T1","T2"],"var1_fi","fi")
    
    pxfile.timeval.set("A1",["T1","T2"],"var3_sv","sv")
    pxfile.timeval.set("A1",["T1","T2"],"var3_fi","fi")

    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword TIMEVAL: Should only reference 1 variable. Found 2: index 0 and 2." in val_rep.error_msg


def test_check_completeness_one_variable_fails_2_half_variables():
    pxfile = _get_model()
    pxfile.timeval.set("A1",["T1","T2"],"var1_sv","sv")
    pxfile.timeval.set("A1",["T1","T2"],"var3_fi","fi")

    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword TIMEVAL: Should only reference 1 variable. Found 2: index 0 and 2." in val_rep.error_msg



def test_check_completeness_lang_fails_missing_lang():
    pxfile = _get_model()
    pxfile.contents.set("My fi contents","fi")

    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword CONTENTS:Missing value for lang:sv" in val_rep.error_msg

def test_check_completeness_each_variable_fails_missing_lang():
    pxfile = _get_model()
    pxfile.doublecolumn.set(True,"var1_sv","sv")
    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword DOUBLECOLUMN:Missing value for variable:var1_fi and lang:fi" in val_rep.error_msg


def test_check_completeness_each_var_value_fails_missing_value():
    pxfile = _get_model()
    pxfile.precision.set(2, "var3_sv", "v_3_1_sv", "sv")
    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword PRECISION:Missing value for variable:var3_fi,value: v_3_1_fi and lang:fi" in val_rep.error_msg


def test_check_completeness_all_variables_fails_missing_value():
    pxfile = _get_model()
    pxfile.variable_type.set("type1","var1_sv","sv")
    pxfile.variable_type.set("C","var2_sv","sv")
    pxfile.variable_type.set("type1","var3_sv","sv")

    pxfile.variable_type.set("type1","var1_fi","fi")
    pxfile.variable_type.set("type1","var3_fi","fi")


    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword VARIABLE-TYPE:Missing value for variable:var2_fi and lang:fi" in val_rep.error_msg

def test_check_completeness_all_content_fails_missing_contvalue():
    pxfile = _get_model()
    pxfile.dayadj.set(True,"v_2_1_fi","fi")
    pxfile.dayadj.set(True,"v_2_2_sv","sv")
    pxfile.dayadj.set(True,"v_2_2_fi","fi")

    val_rep = check_completeness(pxfile)
    assert val_rep.is_valid == False 
    assert "For keyword DAYADJ:Missing value for content:v_2_1_sv and lang:sv" in val_rep.error_msg    


def test_check_completeness_ok():
    pxfile = _get_model()
   
    val_rep = check_completeness(pxfile)
    if not val_rep.is_valid:
        print(val_rep.error_msg) 
    assert val_rep.is_valid