import pytest
from pxbuild.models.output.pxfile.keywords._matrix import _Matrix


def test_matrix_set_valid():
    obj = _Matrix()
    assert not obj.has_value()
    obj.set("a string")
    assert obj.has_value()
    assert obj.get_value() == "a string"


def test_matrix_duplicate_set_raises():
    obj = _Matrix()
    obj.set("a string")
    with pytest.raises(ValueError):
        obj.set("a string")
