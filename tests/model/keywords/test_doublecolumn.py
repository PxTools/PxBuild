import pytest
from pxtool.model.keywords._doublecolumn import _Doublecolumn
    
def test_Doublecolumn_set_valid():
    obj = _Doublecolumn()
    obj.set(True,"region","no")
    assert obj.get_value("region","no") == True
    
def test_Doublecolumn_used_languages():
    obj = _Doublecolumn()
    obj.set(True,"region","no")
    assert "no" in obj.get_used_languages()

def test_Doublecolumn_reset_language():
    obj = _Doublecolumn()
    obj.set(True,"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Doublecolumn_duplicate_set_raises():
    obj = _Doublecolumn()
    obj.set(True,"region","no")
    with pytest.raises(Exception):
        obj.set(True,"region","no")
