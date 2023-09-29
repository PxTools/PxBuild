import pytest
from pxtool.models.output.pxfile.keywords._precision import _Precision
    
def test_Precision_set_valid():
    obj = _Precision()
    assert not obj.has_value("region","oslo","no")    
    obj.set(1,"region","oslo","no")
    assert obj.has_value("region","oslo","no")    
    assert obj.get_value("region","oslo","no") == 1
    
def test_Precision_set_invalid_raises():
    obj = _Precision()
    with pytest.raises(Exception):
       obj.set(666)
    
def test_Precision_used_languages():
    obj = _Precision()
    obj.set(1,"region","oslo","no")
    assert "no" in obj.get_used_languages()

def test_Precision_reset_language():
    obj = _Precision()
    obj.set(1,"region","oslo")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Precision_duplicate_set_raises():
    obj = _Precision()
    obj.set(1,"region","oslo","no")
    with pytest.raises(Exception):
        obj.set(1,"region","oslo","no")
