import pytest
from pxtool.model.keywords._seasadj import _Seasadj
    
def test_Seasadj_set_valid():
    obj = _Seasadj()
    assert not obj.has_value("persons","no")    
    obj.set(True,"persons","no")
    assert obj.has_value("persons","no")    
    assert obj.get_value("persons","no") == True
    
def test_Seasadj_used_languages():
    obj = _Seasadj()
    obj.set(True,"persons","no")
    assert "no" in obj.get_used_languages()

def test_Seasadj_reset_language():
    obj = _Seasadj()
    obj.set(True,"persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Seasadj_duplicate_set_raises():
    obj = _Seasadj()
    obj.set(True,"persons","no")
    with pytest.raises(Exception):
        obj.set(True,"persons","no")
