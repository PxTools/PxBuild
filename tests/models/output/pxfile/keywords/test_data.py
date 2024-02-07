import pytest
from pxbuild.models.output.pxfile.keywords._data import _Data


def test_data_set_valid():
    obj = _Data()
    obj.set(["a string", "no"], 1)
    assert obj.get_value() == ["a string", "no"]


# very TODO


def test_data_duplicate_set_raises():
    obj = _Data()
    obj.set(["a string", "no"], 1)
    with pytest.raises(Exception):
        obj.set(["a string", "no"], 1)
