import pytest
from pxtool.model.keywords._update_frequency import _UpdateFrequency
    
def test_UpdateFrequency_set_valid():
    obj = _UpdateFrequency("UPDATE-FREQUENCY")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_UpdateFrequency_duplicate_set_raises():
    obj = _UpdateFrequency("UPDATE-FREQUENCY")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
