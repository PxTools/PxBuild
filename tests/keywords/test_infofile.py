import pytest
from pxtool.model.keywords._infofile import _Infofile
    
def test_Infofile_set_valid():
    obj = _Infofile("INFOFILE")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Infofile_duplicate_set_raises():
    obj = _Infofile("INFOFILE")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
