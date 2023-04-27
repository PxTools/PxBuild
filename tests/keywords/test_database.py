import pytest
from pxtool.model.keywords._database import _Database
    
def test_Database_set_valid():
    obj = _Database("DATABASE")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Database_duplicate_set_raises():
    obj = _Database("DATABASE")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
