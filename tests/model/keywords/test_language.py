import pytest
from pxtool.models.output.pxfile.keywords._language import _Language
    
def test_Language_set_valid():
    obj = _Language()
    assert not obj.has_value()   
    obj.set("en")
    assert obj.has_value()    
    assert obj.get_value() == "en"
    
def test_Language_set_invalid_raises():
    obj = _Language()
    with pytest.raises(Exception):
       obj.set("bad_string")
    
def test_Language_duplicate_set_raises():
    obj = _Language()
    obj.set("en")
    with pytest.raises(Exception):
        obj.set("en")
