import pytest
from pxtool.models.output.pxfile.keywords._codes import _Codes
    
def test_Codes_set_valid():
    obj = _Codes()
    assert not obj.has_value("region","no")    
    obj.set(["a string"],"region","no")
    assert obj.has_value("region","no")    
    assert obj.get_value("region","no") == ["a string"]
    
def test_Codes_used_languages():
    obj = _Codes()
    obj.set(["a string"],"region","no")
    assert "no" in obj.get_used_languages()

def test_Codes_reset_language():
    obj = _Codes()
    obj.set(["a string"],"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Codes_duplicate_set_raises():
    obj = _Codes()
    obj.set(["a string"],"region","no")
    with pytest.raises(Exception):
        obj.set(["a string"],"region","no")
