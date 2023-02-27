import pytest
from pxtool.model.keywords._axis_version import _PX_AXIS_VERSION

class TestPXAxisVersion:
    def test_set_invalid_axis_version(self):
        axis_version_obj = _PX_AXIS_VERSION("AXIS-VERSION")
        with pytest.raises(ValueError):
            axis_version_obj.set("20221")

        with pytest.raises(ValueError):
            axis_version_obj.set("202a")

def test_px_axis_version_init():
    version = _PX_AXIS_VERSION("AXIS-VERSION")
    assert version._keyword == "AXIS-VERSION"
    assert version.pxvalue_type == "_PxString"
    assert version.is_language_dependent == False

def test_px_axis_version_set_valid():
    version = _PX_AXIS_VERSION("AXIS-VERSION")
    version.set("2022")
    assert version.get() == "2022"

def test_px_axis_version_set_invalid():
    version = _PX_AXIS_VERSION("AXIS-VERSION")
    with pytest.raises(Exception):
        version.set("invalid version")

