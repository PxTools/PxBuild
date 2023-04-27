import pytest
from pxtool.model.keywords._codepage import _Codepage
    
def test_Codepage_set_valid():
    obj = _Codepage("CODEPAGE")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_Codepage_duplicate_set_raises():
    obj = _Codepage("CODEPAGE")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
