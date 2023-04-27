import pytest
from pxtool.model.keywords._datanotesum import _Datanotesum
    
def test_Datanotesum_set_valid():
    obj = _Datanotesum("DATANOTESUM")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datanotesum_duplicate_set_raises():
    obj = _Datanotesum("DATANOTESUM")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
