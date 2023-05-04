import pytest
from pxtool.model.keywords._prestext import _Prestext
    
def test_Prestext_set_valid():
    obj = _Prestext()
    obj.set(1,"region","no")
    assert obj.get_value("region","no") == 1
    
def test_Prestext_set_invalid_raises():
    obj = _Prestext()
    with pytest.raises(Exception):
       obj.set(666)
    
def test_Prestext_used_languages():
    obj = _Prestext()
    obj.set(1,"region","no")
    assert "no" in obj.get_used_languages()

def test_Prestext_reset_language():
    obj = _Prestext()
    obj.set(1,"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Prestext_duplicate_set_raises():
    obj = _Prestext()
    obj.set(1,"region","no")
    with pytest.raises(Exception):
        obj.set(1,"region","no")
