import pytest
from pxtool.model.keywords._refperiod import _Refperiod
    
def test_Refperiod_set_valid():
    obj = _Refperiod()
    obj.set("a string","persons","no")
    assert obj.get_value("persons","no") == "a string"
    
def test_Refperiod_used_languages():
    obj = _Refperiod()
    obj.set("a string","persons","no")
    assert "no" in obj.get_used_languages()

def test_Refperiod_reset_language():
    obj = _Refperiod()
    obj.set("a string","persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Refperiod_duplicate_set_raises():
    obj = _Refperiod()
    obj.set("a string","persons","no")
    with pytest.raises(Exception):
        obj.set("a string","persons","no")
