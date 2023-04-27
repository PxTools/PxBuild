import pytest
from pxtool.model.keywords._copyright import _Copyright
    
def test_Copyright_set_valid():
    obj = _Copyright("COPYRIGHT")
    obj.set(True)
    assert obj.get_value() == True
    
def test_Copyright_duplicate_set_raises():
    obj = _Copyright("COPYRIGHT")
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
