import pytest
from pxtool.model.keywords._datasymbol5 import _Datasymbol5
    
def test_Datasymbol5_set_valid():
    obj = _Datasymbol5()
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol5_used_languages():
    obj = _Datasymbol5()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Datasymbol5_reset_language():
    obj = _Datasymbol5()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Datasymbol5_duplicate_set_raises():
    obj = _Datasymbol5()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
