import pytest
from pxtool.model.keywords._directory_path import _DirectoryPath
    
def test_DirectoryPath_set_valid():
    obj = _DirectoryPath("DIRECTORY-PATH")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_DirectoryPath_duplicate_set_raises():
    obj = _DirectoryPath("DIRECTORY-PATH")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
