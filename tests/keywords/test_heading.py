import pytest
from pxtool.model.keywords._heading import _Heading
    
def test_Heading_set_valid():
    obj = _Heading()
    obj.set(["a string"],"no")
    assert obj.get_value("no") == ["a string"]
    
def test_Heading_used_languages():
    obj = _Heading()
    obj.set(["a string"],"no")
    assert "no" in obj.get_used_languages()

def test_Heading_reset_language():
    obj = _Heading()
    obj.set(["a string"],)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Heading_duplicate_set_raises():
    obj = _Heading()
    obj.set(["a string"],"no")
    with pytest.raises(Exception):
        obj.set(["a string"],"no")
