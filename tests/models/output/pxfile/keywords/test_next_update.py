﻿import pytest
from pxbuild.models.output.pxfile.keywords._next_update import _NextUpdate


def test_nextupdate_set_valid():
    obj = _NextUpdate()
    assert not obj.has_value()
    obj.set("a string")
    assert obj.has_value()
    assert obj.get_value() == "a string"


def test_nextupdate_duplicate_set_raises():
    obj = _NextUpdate()
    obj.set("a string")
    with pytest.raises(ValueError):
        obj.set("a string")
