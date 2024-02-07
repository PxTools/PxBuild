import pytest
from pxbuild.models.output.pxfile.keywords._cfprices import _Cfprices


def test_cfprices_set_valid():
    obj = _Cfprices()
    assert not obj.has_value("persons", "no")
    obj.set("F", "persons", "no")
    assert obj.has_value("persons", "no")
    assert obj.get_value("persons", "no") == "F"


def test_cfprices_used_languages():
    obj = _Cfprices()
    obj.set("F", "persons", "no")
    assert "no" in obj.get_used_languages()


def test_cfprices_reset_language():
    obj = _Cfprices()
    obj.set("F", "persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_cfprices_duplicate_set_raises():
    obj = _Cfprices()
    obj.set("F", "persons", "no")
    with pytest.raises(Exception):
        obj.set("F", "persons", "no")
