import pytest
from pxtool.model.keywords._datasymbol6 import _Datasymbol6
    
def test_Datasymbol6_set_valid():
    obj = _Datasymbol6()
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol6_used_languages():
    obj = _Datasymbol6()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Datasymbol6_reset_language():
    obj = _Datasymbol6()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Datasymbol6_duplicate_set_raises():
    obj = _Datasymbol6()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
