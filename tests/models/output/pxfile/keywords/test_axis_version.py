﻿import pytest
from pxbuild.models.output.pxfile.keywords._axis_version import _AxisVersion


def test_axisversion_set_valid():
    obj = _AxisVersion()
    assert not obj.has_value()
    obj.set("2222")
    assert obj.has_value()
    assert obj.get_value() == "2222"


def test_axisversion_set_invalid_raises():
    obj = _AxisVersion()
    with pytest.raises(ValueError):
        obj.set("bad_string")


def test_axisversion_duplicate_set_raises():
    obj = _AxisVersion()
    obj.set("2222")
    with pytest.raises(ValueError):
        obj.set("2222")
