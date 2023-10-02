import pytest
from pxtool.models.output.pxfile.keywords._tableid import _Tableid
    
def test_Tableid_set_valid():
    obj = _Tableid()
    assert not obj.has_value()   
    obj.set("a string")
    assert obj.has_value()    
    assert obj.get_value() == "a string"
    
def test_Tableid_duplicate_set_raises():
    obj = _Tableid()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
