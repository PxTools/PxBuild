import pytest
from pxbuild.models.output.pxfile.keywords._directory_path import _DirectoryPath


def test_DirectoryPath_set_valid():
    obj = _DirectoryPath()
    assert not obj.has_value()
    obj.set("a string")
    assert obj.has_value()
    assert obj.get_value() == "a string"


def test_DirectoryPath_duplicate_set_raises():
    obj = _DirectoryPath()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
