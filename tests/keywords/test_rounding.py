import pytest
from pxtool.model.keywords._rounding import _Rounding
    
def test_Rounding_set_valid():
    obj = _Rounding("ROUNDING")
    obj.set(1)
    assert obj.get_value() == 1
    
def test_Rounding_duplicate_set_raises():
    obj = _Rounding("ROUNDING")
    obj.set(1)
    with pytest.raises(Exception):
        obj.set(1)
