import pytest
from pxtool.model.keywords._synonyms import _Synonyms
    
def test_Synonyms_set_valid():
    obj = _Synonyms()
    obj.set(["a string"])
    assert obj.get_value() == ["a string"]
    
def test_Synonyms_duplicate_set_raises():
    obj = _Synonyms()
    obj.set(["a string"])
    with pytest.raises(Exception):
        obj.set(["a string"])
