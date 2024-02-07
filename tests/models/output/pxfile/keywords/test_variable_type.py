import pytest
from pxbuild.models.output.pxfile.keywords._variable_type import _VariableType


def test_variabletype_set_valid():
    obj = _VariableType()
    assert not obj.has_value("region", "no")
    obj.set("a string", "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == "a string"


def test_variabletype_used_languages():
    obj = _VariableType()
    obj.set("a string", "region", "no")
    assert "no" in obj.get_used_languages()


def test_variabletype_reset_language():
    obj = _VariableType()
    obj.set("a string", "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_variabletype_duplicate_set_raises():
    obj = _VariableType()
    obj.set("a string", "region", "no")
    with pytest.raises(ValueError):
        obj.set("a string", "region", "no")
