import pytest
from pxbuild.models.output.pxfile.keywords._keys import _Keys


def test_keys_set_valid():
    obj = _Keys()
    assert not obj.has_value("region", "no")
    obj.set("CODES", "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == "CODES"


def test_keys_used_languages():
    obj = _Keys()
    obj.set("CODES", "region", "no")
    assert "no" in obj.get_used_languages()


def test_keys_reset_language():
    obj = _Keys()
    obj.set("CODES", "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_keys_duplicate_set_raises():
    obj = _Keys()
    obj.set("CODES", "region", "no")
    with pytest.raises(Exception):
        obj.set("CODES", "region", "no")
