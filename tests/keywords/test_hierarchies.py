import pytest
from pxtool.model.keywords._hierarchies import _Hierarchies
    
def test_Hierarchies_set_valid():
    obj = _Hierarchies()
    
    obj.set("E25",{"E25":"E15","E15":"E12"}, "region","no")
    assert obj.get_value("region","no") == ("E25",{"E25":"E15","E15":"E12"})
    
def test_Hierarchies_used_languages():
    obj = _Hierarchies()
    obj.set("E25",{"E25":"E15","E15":"E12"}, "region","no")
    assert "no" in obj.get_used_languages()

def test_Hierarchies_reset_language():
    obj = _Hierarchies()
    obj.set("E25",{"E25":"E15","E15":"E12"},"region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Hierarchies_duplicate_set_raises():
    obj = _Hierarchies()
    obj.set("E25",{"E25":"E15","E15":"E12"}, "region","no")
    with pytest.raises(Exception):
        obj.set("E25",{"E25":"E15","E15":"E12"}, "region","no")
