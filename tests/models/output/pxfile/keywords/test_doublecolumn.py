import pytest
from pxbuild.models.output.pxfile.keywords._doublecolumn import _Doublecolumn


def test_doublecolumn_set_valid():
    obj = _Doublecolumn()
    assert not obj.has_value("region", "no")
    obj.set(True, "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == True


def test_doublecolumn_used_languages():
    obj = _Doublecolumn()
    obj.set(True, "region", "no")
    assert "no" in obj.get_used_languages()


def test_doublecolumn_reset_language():
    obj = _Doublecolumn()
    obj.set(True, "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_doublecolumn_duplicate_set_raises():
    obj = _Doublecolumn()
    obj.set(True, "region", "no")
    with pytest.raises(Exception):
        obj.set(True, "region", "no")
