import pytest
from pxtool.model.keywords._attribute_id import _AttributeId
    
def test_AttributeId_set_valid():
    obj = _AttributeId()
    obj.set(["a string"])
    assert obj.get_value() == ["a string"]
    
def test_AttributeId_duplicate_set_raises():
    obj = _AttributeId()
    obj.set(["a string"])
    with pytest.raises(Exception):
        obj.set(["a string"])
