import pytest
from pxbuild.models.output.pxfile.keywords._datasymbol4 import _Datasymbol4


def test_datasymbol4_set_valid():
    obj = _Datasymbol4()
    assert not obj.has_value("no")
    obj.set("a string", "no")
    assert obj.has_value("no")
    assert obj.get_value("no") == "a string"


def test_datasymbol4_used_languages():
    obj = _Datasymbol4()
    obj.set("a string", "no")
    assert "no" in obj.get_used_languages()


def test_datasymbol4_reset_language():
    obj = _Datasymbol4()
    obj.set(
        "a string",
    )
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_datasymbol4_duplicate_set_raises():
    obj = _Datasymbol4()
    obj.set("a string", "no")
    with pytest.raises(Exception):
        obj.set("a string", "no")
