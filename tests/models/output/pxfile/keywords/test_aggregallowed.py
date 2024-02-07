import pytest
from pxbuild.models.output.pxfile.keywords._aggregallowed import _Aggregallowed


def test_aggregallowed_set_valid():
    obj = _Aggregallowed()
    assert not obj.has_value()
    obj.set(True)
    assert obj.has_value()
    assert obj.get_value() == True


def test_aggregallowed_duplicate_set_raises():
    obj = _Aggregallowed()
    obj.set(True)
    with pytest.raises(ValueError):
        obj.set(True)
