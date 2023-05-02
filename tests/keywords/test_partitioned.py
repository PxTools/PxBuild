import pytest
from pxtool.model.keywords._partitioned import _Partitioned
    
def test_Partitioned_set_valid():
    obj = _Partitioned()
    obj.set(["a string"],"region","no")
    assert obj.get_value("region","no") == ["a string"]
    
def test_Partitioned_used_languages():
    obj = _Partitioned()
    obj.set(["a string"],"region","no")
    assert "no" in obj.get_used_languages()

def test_Partitioned_reset_language():
    obj = _Partitioned()
    obj.set(["a string"],"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

