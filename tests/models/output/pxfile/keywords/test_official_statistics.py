import pytest
from pxbuild.models.output.pxfile.keywords._official_statistics import _OfficialStatistics


def test_OfficialStatistics_set_valid():
    obj = _OfficialStatistics()
    assert not obj.has_value()
    obj.set(True)
    assert obj.has_value()
    assert obj.get_value() == True


def test_OfficialStatistics_duplicate_set_raises():
    obj = _OfficialStatistics()
    obj.set(True)
    with pytest.raises(Exception):
        obj.set(True)
