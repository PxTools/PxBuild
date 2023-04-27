import pytest
from pxtool.model.keywords._datasymbol2 import _Datasymbol2
    
def test_Datasymbol2_set_valid():
    obj = _Datasymbol2("DATASYMBOL2")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol2_duplicate_set_raises():
    obj = _Datasymbol2("DATASYMBOL2")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
