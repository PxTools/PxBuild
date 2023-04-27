import pytest
from pxtool.model.keywords._datasymbolnil import _Datasymbolnil
    
def test_Datasymbolnil_set_valid():
    obj = _Datasymbolnil("DATASYMBOLNIL")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Datasymbolnil_duplicate_set_raises():
    obj = _Datasymbolnil("DATASYMBOLNIL")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
