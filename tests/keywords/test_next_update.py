import pytest
from pxtool.model.keywords._next_update import _NextUpdate
    
def test_NextUpdate_set_valid():
    obj = _NextUpdate("NEXT-UPDATE")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_NextUpdate_duplicate_set_raises():
    obj = _NextUpdate("NEXT-UPDATE")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
