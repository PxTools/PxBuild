import pytest
from pxtool.model.keywords._languages import _Languages
    
def test_Languages_set_valid():
    obj = _Languages("LANGUAGES")
    obj.set(["en"])
    assert obj.get_value() == ["en"]
    
def test_Languages_set_invalid_raises():
    obj = _Languages("LANGUAGES")
    with pytest.raises(Exception):
       obj.set(["bad_string"])
    
def test_Languages_duplicate_set_raises():
    obj = _Languages("LANGUAGES")
    obj.set(["en"])
    with pytest.raises(Exception):
        obj.set(["en"])
