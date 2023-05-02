import pytest
from pxtool.model.keywords._confidential import _Confidential
    
def test_Confidential_set_valid():
    obj = _Confidential()
    obj.set(1)
    assert obj.get_value() == 1
    
def test_Confidential_duplicate_set_raises():
    obj = _Confidential()
    obj.set(1)
    with pytest.raises(Exception):
        obj.set(1)
