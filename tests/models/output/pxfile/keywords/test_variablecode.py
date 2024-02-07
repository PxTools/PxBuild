import pytest
from pxbuild.models.output.pxfile.keywords._variablecode import _Variablecode


def test_variablecode_set_valid():
    obj = _Variablecode()
    assert not obj.has_value("region", "no")
    obj.set("a string", "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == "a string"


def test_variablecode_used_languages():
    obj = _Variablecode()
    obj.set("a string", "region", "no")
    assert "no" in obj.get_used_languages()


def test_variablecode_reset_language():
    obj = _Variablecode()
    obj.set("a string", "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_variablecode_duplicate_set_raises():
    obj = _Variablecode()
    obj.set("a string", "region", "no")
    with pytest.raises(Exception):
        obj.set("a string", "region", "no")
