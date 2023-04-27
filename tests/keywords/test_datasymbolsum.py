import pytest
from pxtool.model.keywords._datasymbolsum import _Datasymbolsum
    
def test_Datasymbolsum_set_valid():
    obj = _Datasymbolsum("DATASYMBOLSUM")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbolsum_duplicate_set_raises():
    obj = _Datasymbolsum("DATASYMBOLSUM")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
