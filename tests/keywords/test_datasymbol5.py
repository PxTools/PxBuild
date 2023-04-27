import pytest
from pxtool.model.keywords._datasymbol5 import _Datasymbol5
    
def test_Datasymbol5_set_valid():
    obj = _Datasymbol5("DATASYMBOL5")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol5_duplicate_set_raises():
    obj = _Datasymbol5("DATASYMBOL5")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
