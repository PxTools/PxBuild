import pytest
from pxbuild.models.output.pxfile.keywords._stub import _Stub


def test_stub_set_valid():
    obj = _Stub()
    assert not obj.has_value("no")
    obj.set(["a string"], "no")
    assert obj.has_value("no")
    assert obj.get_value("no") == ["a string"]


def test_stub_used_languages():
    obj = _Stub()
    obj.set(["a string"], "no")
    assert "no" in obj.get_used_languages()


def test_stub_reset_language():
    obj = _Stub()
    obj.set(
        ["a string"],
    )
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_stub_duplicate_set_raises():
    obj = _Stub()
    obj.set(["a string"], "no")
    with pytest.raises(ValueError):
        obj.set(["a string"], "no")
