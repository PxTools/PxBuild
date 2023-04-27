import pytest
from pxtool.model.keywords._datasymbol4 import _Datasymbol4
    
def test_Datasymbol4_set_valid():
    obj = _Datasymbol4("DATASYMBOL4")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol4_duplicate_set_raises():
    obj = _Datasymbol4("DATASYMBOL4")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
