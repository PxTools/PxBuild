import pytest
from pxtool.model.keywords._first_published import _FirstPublished
    
def test_FirstPublished_set_valid():
    obj = _FirstPublished("FIRST-PUBLISHED")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_FirstPublished_duplicate_set_raises():
    obj = _FirstPublished("FIRST-PUBLISHED")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
