import pytest
from pxtool.models.output.pxfile.keywords._attribute_id import _AttributeId
    
def test_AttributeId_set_valid():
    obj = _AttributeId()
    assert not obj.has_value()   
    obj.set(["a string"])
    assert obj.has_value()    
    assert obj.get_value() == ["a string"]
    
def test_AttributeId_duplicate_set_raises():
    obj = _AttributeId()
    obj.set(["a string"])
    with pytest.raises(Exception):
        obj.set(["a string"])
