import pytest
from pxbuild.models.output.pxfile.keywords._confidential import _Confidential


def test_confidential_set_valid():
    obj = _Confidential()
    assert not obj.has_value()
    obj.set(1)
    assert obj.has_value()
    assert obj.get_value() == 1


def test_confidential_duplicate_set_raises():
    obj = _Confidential()
    obj.set(1)
    with pytest.raises(ValueError):
        obj.set(1)
