import pytest
from pxtool.model.keywords._hierarchynames import _Hierarchynames
    
def test_Hierarchynames_set_valid():
    obj = _Hierarchynames()
    assert not obj.has_value("region","no")    
    obj.set(["a string"],"region","no")
    assert obj.has_value("region","no")    
    assert obj.get_value("region","no") == ["a string"]
    
def test_Hierarchynames_used_languages():
    obj = _Hierarchynames()
    obj.set(["a string"],"region","no")
    assert "no" in obj.get_used_languages()

def test_Hierarchynames_reset_language():
    obj = _Hierarchynames()
    obj.set(["a string"],"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Hierarchynames_duplicate_set_raises():
    obj = _Hierarchynames()
    obj.set(["a string"],"region","no")
    with pytest.raises(Exception):
        obj.set(["a string"],"region","no")
