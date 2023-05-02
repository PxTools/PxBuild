import pytest
from pxtool.model.keywords._timeval import _Timeval
    
def test_Timeval_set_valid():
    obj = _Timeval()
    
    obj.set("A1",["1994","1995","1996"], "time","no")
    assert obj.get_value("time","no") == ("A1",["1994","1995","1996"])
    
def test_Timeval_used_languages():
    obj = _Timeval()
    obj.set("A1",["1994","1995","1996"], "time","no")
    assert "no" in obj.get_used_languages()

def test_Timeval_reset_language():
    obj = _Timeval()
    obj.set("A1",["1994","1995","1996"],"time")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Timeval_duplicate_set_raises():
    obj = _Timeval()
    obj.set("A1",["1994","1995","1996"], "time","no")
    with pytest.raises(Exception):
        obj.set("A1",["1994","1995","1996"], "time","no")
