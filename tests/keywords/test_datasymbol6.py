import pytest
from pxtool.model.keywords._datasymbol6 import _Datasymbol6
    
def test_Datasymbol6_set_valid():
    obj = _Datasymbol6("DATASYMBOL6")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol6_duplicate_set_raises():
    obj = _Datasymbol6("DATASYMBOL6")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
