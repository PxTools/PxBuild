import pytest
from pxtool.model.keywords._hierarchylevels import _Hierarchylevels
    
def test_Hierarchylevels_set_valid():
    obj = _Hierarchylevels()
    obj.set(3,"region","no")
    assert obj.get_value("region","no") == 3
    
def test_Hierarchylevels_used_languages():
    obj = _Hierarchylevels()
    obj.set(3,"region","no")
    assert "no" in obj.get_used_languages()

def test_Hierarchylevels_reset_language():
    obj = _Hierarchylevels()
    obj.set(3,"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Hierarchylevels_duplicate_set_raises():
    obj = _Hierarchylevels()
    obj.set(3,"region","no")
    with pytest.raises(Exception):
        obj.set(3,"region","no")
