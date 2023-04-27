import pytest
from pxtool.model.keywords._datasymbol3 import _Datasymbol3
    
def test_Datasymbol3_set_valid():
    obj = _Datasymbol3("DATASYMBOL3")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbol3_duplicate_set_raises():
    obj = _Datasymbol3("DATASYMBOL3")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
