import pytest
from pxbuild.models.output.pxfile.keywords._descriptiondefault import _Descriptiondefault
    
def test_Descriptiondefault_set_valid():
    obj = _Descriptiondefault()
    assert not obj.has_value()   
    obj.set(True)
    assert obj.has_value()    
    assert obj.get_value() == True
    
def test_Descriptiondefault_duplicate_set_raises():
    obj = _Descriptiondefault()
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
