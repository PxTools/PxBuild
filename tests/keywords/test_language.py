import pytest
from pxtool.model.keywords._language import _Language
    
def test_Language_set_valid():
    obj = _Language("LANGUAGE")
    obj.set("en")
    assert obj.get_value() == "en"
    
def test_Language_set_invalid_raises():
    obj = _Language("LANGUAGE")
    with pytest.raises(Exception):
       obj.set("bad_string")
    
def test_Language_duplicate_set_raises():
    obj = _Language("LANGUAGE")
    obj.set("en")
    with pytest.raises(Exception):
        obj.set("en")
