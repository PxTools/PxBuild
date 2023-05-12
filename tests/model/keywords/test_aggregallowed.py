import pytest
from pxtool.model.keywords._aggregallowed import _Aggregallowed
    
def test_Aggregallowed_set_valid():
    obj = _Aggregallowed()
    assert not obj.has_value()   
    obj.set(True)
    assert obj.has_value()    
    assert obj.get_value() == True
    
def test_Aggregallowed_duplicate_set_raises():
    obj = _Aggregallowed()
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
