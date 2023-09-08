import pytest
from pxtool.model.keywords._dayadj import _Dayadj
    
def test_Dayadj_set_valid():
    obj = _Dayadj()
    assert not obj.has_value("persons","no")    
    obj.set(True,"persons","no")
    assert obj.has_value("persons","no")    
    assert obj.get_value("persons","no") == True
    
def test_Dayadj_used_languages():
    obj = _Dayadj()
    obj.set(True,"persons","no")
    assert "no" in obj.get_used_languages()

def test_Dayadj_reset_language():
    obj = _Dayadj()
    obj.set(True,"persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Dayadj_duplicate_set_raises():
    obj = _Dayadj()
    obj.set(True,"persons","no")
    with pytest.raises(Exception):
        obj.set(True,"persons","no")
