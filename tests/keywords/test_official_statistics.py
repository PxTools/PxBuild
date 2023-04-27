import pytest
from pxtool.model.keywords._official_statistics import _OfficialStatistics
    
def test_OfficialStatistics_set_valid():
    obj = _OfficialStatistics("OFFICIAL-STATISTICS")
    obj.set(True)
    assert obj.get_value() == True
    
def test_OfficialStatistics_duplicate_set_raises():
    obj = _OfficialStatistics("OFFICIAL-STATISTICS")
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
