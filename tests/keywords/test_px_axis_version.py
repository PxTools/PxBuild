import pytest
from pxtool.model.keywords._axis_version import _AxisVersion

class TestPXAxisVersion:
    def test_set_invalid_axis_version(self):
        axis_version_obj = _AxisVersion("AXIS-VERSION")
        with pytest.raises(ValueError):
            axis_version_obj.set("20221")

        with pytest.raises(ValueError):
            axis_version_obj.set("202a")

def test_AxisVersion_init():
    version = _AxisVersion("AXIS-VERSION")
    assert version._keyword == "AXIS-VERSION"
    assert version.pxvalue_type == "_PxString"
    assert version.is_language_dependent == False

def test_AxisVersion_set_valid():
    version = _AxisVersion("AXIS-VERSION")
    version.set("2022")
    assert version.get_value() == "2022"

def test_AxisVersion_set_invalid():
    version = _AxisVersion("AXIS-VERSION")
    with pytest.raises(Exception):
        version.set("invalid version")

