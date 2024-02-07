import pytest
from pxbuild.models.output.pxfile.keywords._datasymbol3 import _Datasymbol3


def test_datasymbol3_set_valid():
    obj = _Datasymbol3()
    assert not obj.has_value("no")
    obj.set("a string", "no")
    assert obj.has_value("no")
    assert obj.get_value("no") == "a string"


def test_datasymbol3_used_languages():
    obj = _Datasymbol3()
    obj.set("a string", "no")
    assert "no" in obj.get_used_languages()


def test_datasymbol3_reset_language():
    obj = _Datasymbol3()
    obj.set(
        "a string",
    )
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_datasymbol3_duplicate_set_raises():
    obj = _Datasymbol3()
    obj.set("a string", "no")
    with pytest.raises(Exception):
        obj.set("a string", "no")
