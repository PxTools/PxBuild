import pytest
from pxtool.model.keywords._charset import _Charset
    
def test_Charset_set_valid():
    obj = _Charset()
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_Charset_duplicate_set_raises():
    obj = _Charset()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
