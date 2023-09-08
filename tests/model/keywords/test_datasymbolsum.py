import pytest
from pxtool.model.keywords._datasymbolsum import _Datasymbolsum
    
def test_Datasymbolsum_set_valid():
    obj = _Datasymbolsum()
    assert not obj.has_value("no")    
    obj.set("a string","no")
    assert obj.has_value("no")    
    assert obj.get_value("no") == "a string"
    
def test_Datasymbolsum_used_languages():
    obj = _Datasymbolsum()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Datasymbolsum_reset_language():
    obj = _Datasymbolsum()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Datasymbolsum_duplicate_set_raises():
    obj = _Datasymbolsum()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
