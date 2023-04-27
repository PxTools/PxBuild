import pytest
from pxtool.model.keywords._contvariable import _Contvariable
    
def test_Contvariable_set_valid():
    obj = _Contvariable("CONTVARIABLE")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Contvariable_duplicate_set_raises():
    obj = _Contvariable("CONTVARIABLE")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
