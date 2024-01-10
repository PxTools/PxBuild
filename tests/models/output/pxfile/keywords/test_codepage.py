import pytest
from pxbuild.models.output.pxfile.keywords._codepage import _Codepage
    
def test_Codepage_set_valid():
    obj = _Codepage()
    assert not obj.has_value()   
    obj.set("a string")
    assert obj.has_value()    
    assert obj.get_value() == "a string"
    
def test_Codepage_duplicate_set_raises():
    obj = _Codepage()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
