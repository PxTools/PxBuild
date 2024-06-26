﻿import pytest
from pxbuild.models.output.pxfile.keywords._rounding import _Rounding


def test_rounding_set_valid():
    obj = _Rounding()
    assert not obj.has_value()
    obj.set(1)
    assert obj.has_value()
    assert obj.get_value() == 1


def test_rounding_duplicate_set_raises():
    obj = _Rounding()
    obj.set(1)
    with pytest.raises(ValueError):
        obj.set(1)
