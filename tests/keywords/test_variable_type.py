import pytest
from pxtool.model.keywords._variable_type import _VariableType
    
def test_VariableType_set_valid():
    obj = _VariableType()
    obj.set("a string","region","no")
    assert obj.get_value("region","no") == "a string"
    
def test_VariableType_used_languages():
    obj = _VariableType()
    obj.set("a string","region","no")
    assert "no" in obj.get_used_languages()

def test_VariableType_reset_language():
    obj = _VariableType()
    obj.set("a string","region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_VariableType_duplicate_set_raises():
    obj = _VariableType()
    obj.set("a string","region","no")
    with pytest.raises(Exception):
        obj.set("a string","region","no")
