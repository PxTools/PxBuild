import pytest
from pxbuild.models.output.pxfile.keywords._decimals import _Decimals


def test_decimals_set_valid():
    obj = _Decimals()
    assert not obj.has_value()
    obj.set(1)
    assert obj.has_value()
    assert obj.get_value() == 1


def test_decimals_duplicate_set_raises():
    obj = _Decimals()
    obj.set(1)
    with pytest.raises(ValueError):
        obj.set(1)
