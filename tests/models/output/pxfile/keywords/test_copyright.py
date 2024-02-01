import pytest
from pxbuild.models.output.pxfile.keywords._copyright import _Copyright


def test_Copyright_set_valid():
    obj = _Copyright()
    assert not obj.has_value()
    obj.set(True)
    assert obj.has_value()
    assert obj.get_value() == True


def test_Copyright_duplicate_set_raises():
    obj = _Copyright()
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
