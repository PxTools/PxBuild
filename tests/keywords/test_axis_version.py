import pytest
from pxtool.model.keywords._axis_version import _AxisVersion
    
def test_AxisVersion_set_valid():
    obj = _AxisVersion("AXIS-VERSION")
    obj.set("2222")
    assert obj.get_value() == "2222"
    
def test_AxisVersion_set_invalid_raises():
    obj = _AxisVersion("AXIS-VERSION")
    with pytest.raises(Exception):
       obj.set("bad_string")
    
def test_AxisVersion_duplicate_set_raises():
    obj = _AxisVersion("AXIS-VERSION")
    obj.set("2222")
    with pytest.raises(Exception):
        obj.set("2222")
