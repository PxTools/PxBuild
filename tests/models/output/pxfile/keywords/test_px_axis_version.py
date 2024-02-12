import pytest
from pxbuild.models.output.pxfile.keywords._axis_version import _AxisVersion


class TestPXAxisVersion:
    def test_set_invalid_axis_version(self):
        axis_version_obj = _AxisVersion()
        with pytest.raises(ValueError):
            axis_version_obj.set("20221")

        with pytest.raises(ValueError):
            axis_version_obj.set("202a")


def test_axisversion_init():
    version = _AxisVersion()
    assert version._keyword == "AXIS-VERSION"
    assert version.pxvalue_type == "_PxString"
    assert not version.may_have_language


def test_axisversion_set_valid():
    version = _AxisVersion()
    version.set("2022")
    assert version.get_value() == "2022"


def test_axisversion_set_invalid():
    version = _AxisVersion()
    with pytest.raises(ValueError):
        version.set("invalid version")
