import pytest
from pxbuild.models.output.pxfile.keywords._link import _Link
    
def test_Link_set_valid():
    obj = _Link()
    assert not obj.has_value("no")    
    obj.set("a string","no")
    assert obj.has_value("no")    
    assert obj.get_value("no") == "a string"
    
def test_Link_used_languages():
    obj = _Link()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Link_reset_language():
    obj = _Link()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Link_duplicate_set_raises():
    obj = _Link()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
