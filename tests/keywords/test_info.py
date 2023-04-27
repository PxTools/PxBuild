import pytest
from pxtool.model.keywords._info import _Info
    
def test_Info_set_valid():
    obj = _Info("INFO")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Info_duplicate_set_raises():
    obj = _Info("INFO")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
