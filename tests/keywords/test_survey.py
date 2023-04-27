import pytest
from pxtool.model.keywords._survey import _Survey
    
def test_Survey_set_valid():
    obj = _Survey("SURVEY")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Survey_duplicate_set_raises():
    obj = _Survey("SURVEY")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
