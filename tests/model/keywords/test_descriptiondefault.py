import pytest
from pxtool.model.keywords._descriptiondefault import _Descriptiondefault
    
def test_Descriptiondefault_set_valid():
    obj = _Descriptiondefault()
    obj.set(True)
    assert obj.get_value() == True
    
def test_Descriptiondefault_duplicate_set_raises():
    obj = _Descriptiondefault()
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
