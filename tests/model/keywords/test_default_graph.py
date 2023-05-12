import pytest
from pxtool.model.keywords._default_graph import _DefaultGraph
    
def test_DefaultGraph_set_valid():
    obj = _DefaultGraph()
    assert not obj.has_value()   
    obj.set(1)
    assert obj.has_value()    
    assert obj.get_value() == 1
    
def test_DefaultGraph_duplicate_set_raises():
    obj = _DefaultGraph()
    obj.set(1)
    with pytest.raises(Exception):
        obj.set(1)
