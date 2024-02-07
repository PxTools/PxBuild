import pytest
from pxbuild.models.output.pxfile.keywords._elimination import _Elimination


def test_elimination_set_valid():
    obj = _Elimination()
    assert not obj.has_value("region", "no")
    obj.set("a string", "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == "a string"


def test_elimination_used_languages():
    obj = _Elimination()
    obj.set("a string", "region", "no")
    assert "no" in obj.get_used_languages()


def test_elimination_reset_language():
    obj = _Elimination()
    obj.set("a string", "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_elimination_duplicate_set_raises():
    obj = _Elimination()
    obj.set("a string", "region", "no")
    with pytest.raises(ValueError):
        obj.set("a string", "region", "no")
