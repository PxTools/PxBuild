﻿import pytest
from pxbuild.models.output.pxfile.keywords._copyright import _Copyright


def test_copyright_set_valid():
    obj = _Copyright()
    assert not obj.has_value()
    obj.set(True)
    assert obj.has_value()
    assert obj.get_value()


def test_copyright_duplicate_set_raises():
    obj = _Copyright()
    obj.set(True)
    with pytest.raises(ValueError):
        obj.set(True)
