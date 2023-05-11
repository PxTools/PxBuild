import pytest
from pxtool.model.keywords._last_updated import _LastUpdated
    
def test_LastUpdated_set_valid():
    obj = _LastUpdated()
    assert not obj.has_value("persons","no")    
    obj.set("a string","persons","no")
    assert obj.has_value("persons","no")    
    assert obj.get_value("persons","no") == "a string"
    
def test_LastUpdated_used_languages():
    obj = _LastUpdated()
    obj.set("a string","persons","no")
    assert "no" in obj.get_used_languages()

def test_LastUpdated_reset_language():
    obj = _LastUpdated()
    obj.set("a string","persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_LastUpdated_duplicate_set_raises():
    obj = _LastUpdated()
    obj.set("a string","persons","no")
    with pytest.raises(Exception):
        obj.set("a string","persons","no")
