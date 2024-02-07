import pytest
from pxbuild.models.output.pxfile.keywords._baseperiod import _Baseperiod


def test_baseperiod_set_valid():
    obj = _Baseperiod()
    assert not obj.has_value("persons", "no")
    obj.set("a string", "persons", "no")
    assert obj.has_value("persons", "no")
    assert obj.get_value("persons", "no") == "a string"


def test_baseperiod_used_languages():
    obj = _Baseperiod()
    obj.set("a string", "persons", "no")
    assert "no" in obj.get_used_languages()


def test_baseperiod_reset_language():
    obj = _Baseperiod()
    obj.set("a string", "persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_baseperiod_duplicate_set_raises():
    obj = _Baseperiod()
    obj.set("a string", "persons", "no")
    with pytest.raises(Exception):
        obj.set("a string", "persons", "no")
