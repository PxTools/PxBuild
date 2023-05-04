import pytest
from pxtool.model.keywords._elimination import _Elimination
    
def test_Elimination_set_valid():
    obj = _Elimination()
    obj.set("a string","region","no")
    assert obj.get_value("region","no") == "a string"
    
def test_Elimination_used_languages():
    obj = _Elimination()
    obj.set("a string","region","no")
    assert "no" in obj.get_used_languages()

def test_Elimination_reset_language():
    obj = _Elimination()
    obj.set("a string","region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Elimination_duplicate_set_raises():
    obj = _Elimination()
    obj.set("a string","region","no")
    with pytest.raises(Exception):
        obj.set("a string","region","no")
