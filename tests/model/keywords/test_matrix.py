import pytest
from pxtool.model.keywords._matrix import _Matrix
    
def test_Matrix_set_valid():
    obj = _Matrix()
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_Matrix_duplicate_set_raises():
    obj = _Matrix()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
