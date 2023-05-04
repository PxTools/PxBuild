import pytest
from pxtool.model.keywords._data import _Data
    
def test_Data_set_valid():
    obj = _Data()
    obj.set(["a string","no"])
    assert obj.get_value() == ["a string","no"]
    
#very TODO
    
def test_Data_duplicate_set_raises():
    obj = _Data()
    obj.set(["a string","no"])
    with pytest.raises(Exception):
        obj.set(["a string","no"])
