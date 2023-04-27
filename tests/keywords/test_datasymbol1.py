import pytest
from pxtool.model.keywords._datasymbol1 import _Datasymbol1
    
def test_Datasymbol1_set_valid():
    obj = _Datasymbol1("DATASYMBOL1")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol1_duplicate_set_raises():
    obj = _Datasymbol1("DATASYMBOL1")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
