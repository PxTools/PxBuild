import pytest
from pxtool.model.keywords._link import _Link
    
def test_Link_set_valid():
    obj = _Link("LINK")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Link_duplicate_set_raises():
    obj = _Link("LINK")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
