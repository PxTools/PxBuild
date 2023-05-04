import pytest
from pxtool.model.keywords._datasymbol3 import _Datasymbol3
    
def test_Datasymbol3_set_valid():
    obj = _Datasymbol3()
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol3_used_languages():
    obj = _Datasymbol3()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_Datasymbol3_reset_language():
    obj = _Datasymbol3()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Datasymbol3_duplicate_set_raises():
    obj = _Datasymbol3()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
