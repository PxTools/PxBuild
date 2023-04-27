import pytest
from pxtool.model.keywords._source import _Source
    
def test_Source_set_valid():
    obj = _Source("SOURCE")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Source_duplicate_set_raises():
    obj = _Source("SOURCE")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
