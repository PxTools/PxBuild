import pytest
from pxbuild.models.output.pxfile.keywords._stockfa import _Stockfa


def test_stockfa_set_valid():
    obj = _Stockfa()
    assert not obj.has_value("persons", "no")
    obj.set("F", "persons", "no")
    assert obj.has_value("persons", "no")
    assert obj.get_value("persons", "no") == "F"


def test_stockfa_used_languages():
    obj = _Stockfa()
    obj.set("F", "persons", "no")
    assert "no" in obj.get_used_languages()


def test_stockfa_reset_language():
    obj = _Stockfa()
    obj.set("F", "persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_stockfa_duplicate_set_raises():
    obj = _Stockfa()
    obj.set("F", "persons", "no")
    with pytest.raises(Exception):
        obj.set("F", "persons", "no")
