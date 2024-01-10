import pytest
from pxbuild.models.output.pxfile.keywords._contents import _Contents
    
def test_Contents_set_valid():
    obj = _Contents()
    assert not obj.has_value("no")    
    obj.set("a string","no")
    assert obj.has_value("no")    
    assert obj.get_value("no") == "a string"
    
def test_Contents_used_languages():
    obj = _Contents()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Contents_reset_language():
    obj = _Contents()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Contents_duplicate_set_raises():
    obj = _Contents()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
