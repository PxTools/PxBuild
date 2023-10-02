import pytest
from pxtool.models.output.pxfile.keywords._units import _Units
    
def test_Units_set_valid():
    obj = _Units()
    assert not obj.has_value("persons","no")    
    obj.set("a string","persons","no")
    assert obj.has_value("persons","no")    
    assert obj.get_value("persons","no") == "a string"
    
def test_Units_used_languages():
    obj = _Units()
    obj.set("a string","persons","no")
    assert "no" in obj.get_used_languages()

def test_Units_reset_language():
    obj = _Units()
    obj.set("a string","persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Units_duplicate_set_raises():
    obj = _Units()
    obj.set("a string","persons","no")
    with pytest.raises(Exception):
        obj.set("a string","persons","no")
