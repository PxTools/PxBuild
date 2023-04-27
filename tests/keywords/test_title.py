import pytest
from pxtool.model.keywords._title import _Title
    
def test_Title_set_valid():
    obj = _Title("TITLE")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Title_duplicate_set_raises():
    obj = _Title("TITLE")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
