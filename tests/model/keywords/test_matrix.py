import pytest
from pxtool.models.output.pxfile.keywords._matrix import _Matrix
    
def test_Matrix_set_valid():
    obj = _Matrix()
    assert not obj.has_value()   
    obj.set("a string")
    assert obj.has_value()    
    assert obj.get_value() == "a string"
    
def test_Matrix_duplicate_set_raises():
    obj = _Matrix()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
