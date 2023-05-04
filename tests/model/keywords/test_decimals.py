import pytest
from pxtool.model.keywords._decimals import _Decimals
    
def test_Decimals_set_valid():
    obj = _Decimals()
    obj.set(1)
    assert obj.get_value() == 1
    
def test_Decimals_duplicate_set_raises():
    obj = _Decimals()
    obj.set(1)
    with pytest.raises(Exception):
        obj.set(1)
