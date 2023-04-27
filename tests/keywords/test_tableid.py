import pytest
from pxtool.model.keywords._tableid import _Tableid
    
def test_Tableid_set_valid():
    obj = _Tableid("TABLEID")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_Tableid_duplicate_set_raises():
    obj = _Tableid("TABLEID")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
