import pytest
from pxtool.model.keywords._description import _Description
    
def test_Description_set_valid():
    obj = _Description("DESCRIPTION")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Description_duplicate_set_raises():
    obj = _Description("DESCRIPTION")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
