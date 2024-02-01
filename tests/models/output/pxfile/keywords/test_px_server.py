import pytest
from pxbuild.models.output.pxfile.keywords._px_server import _PxServer


def test_PxServer_set_valid():
    obj = _PxServer()
    assert not obj.has_value()
    obj.set("a string")
    assert obj.has_value()
    assert obj.get_value() == "a string"


def test_PxServer_duplicate_set_raises():
    obj = _PxServer()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
