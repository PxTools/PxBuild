import pytest
from pxbuild.models.output.pxfile.keywords._values import _Values


def test_values_set_valid():
    obj = _Values()
    assert not obj.has_value("region", "no")
    obj.set(["a string"], "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == ["a string"]


def test_values_used_languages():
    obj = _Values()
    obj.set(["a string"], "region", "no")
    assert "no" in obj.get_used_languages()


def test_values_reset_language():
    obj = _Values()
    obj.set(["a string"], "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_values_duplicate_set_raises():
    obj = _Values()
    obj.set(["a string"], "region", "no")
    with pytest.raises(Exception):
        obj.set(["a string"], "region", "no")
