import pytest
from pxbuild.models.output.pxfile.keywords._autopen import _Autopen


def test_autopen_set_valid():
    obj = _Autopen()
    assert not obj.has_value()
    obj.set(True)
    assert obj.has_value()
    assert obj.get_value()


def test_autopen_duplicate_set_raises():
    obj = _Autopen()
    obj.set(True)
    with pytest.raises(ValueError):
        obj.set(True)
