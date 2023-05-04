import pytest
from pxtool.model.keywords._meta_id import _MetaId
    
def test_MetaId_set_valid():
    obj = _MetaId()
    obj.set("a string","region","oslo")
    assert obj.get_value("region","oslo") == "a string"

    
def test_MetaId_duplicate_set_raises():
    obj = _MetaId()
    obj.set("a string","region","oslo")
    with pytest.raises(Exception):
        obj.set("a string","region","oslo")
