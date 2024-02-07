import pytest
from pxbuild.models.output.pxfile.keywords._contact import _Contact


def test_contact_set_valid():
    obj = _Contact()
    assert not obj.has_value("persons", "no")
    obj.set("a string", "persons", "no")
    assert obj.has_value("persons", "no")
    assert obj.get_value("persons", "no") == "a string"


def test_contact_used_languages():
    obj = _Contact()
    obj.set("a string", "persons", "no")
    assert "no" in obj.get_used_languages()


def test_contact_reset_language():
    obj = _Contact()
    obj.set("a string", "persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_contact_duplicate_set_raises():
    obj = _Contact()
    obj.set("a string", "persons", "no")
    with pytest.raises(ValueError):
        obj.set("a string", "persons", "no")
