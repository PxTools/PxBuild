import pytest
from pxtool.model.keywords._autopen import _Autopen
    
def test_Autopen_set_valid():
    obj = _Autopen("AUTOPEN")
    obj.set(True)
    assert obj.get_value() == True
    
def test_Autopen_duplicate_set_raises():
    obj = _Autopen("AUTOPEN")
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
