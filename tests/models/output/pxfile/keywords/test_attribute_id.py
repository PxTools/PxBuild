import pytest
from pxbuild.models.output.pxfile.keywords._attribute_id import _AttributeId


def test_attributeid_set_valid():
    obj = _AttributeId()
    assert not obj.has_value()
    obj.set(["a string"])
    assert obj.has_value()
    assert obj.get_value() == ["a string"]


def test_attributeid_duplicate_set_raises():
    obj = _AttributeId()
    obj.set(["a string"])
    with pytest.raises(ValueError):
        obj.set(["a string"])
