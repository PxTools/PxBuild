import pytest
from pxbuild.models.output.pxfile.keywords._meta_id import _MetaId


def test_MetaId_set_valid():
    obj = _MetaId()
    assert not obj.has_value("region", "oslo", "no")
    obj.set("a string", "region", "oslo", "no")
    assert obj.has_value("region", "oslo", "no")
    assert obj.get_value("region", "oslo", "no") == "a string"


def test_MetaId_used_languages():
    obj = _MetaId()
    obj.set("a string", "region", "oslo", "no")
    assert "no" in obj.get_used_languages()


def test_MetaId_reset_language():
    obj = _MetaId()
    obj.set("a string", "region", "oslo")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_MetaId_duplicate_set_raises():
    obj = _MetaId()
    obj.set("a string", "region", "oslo", "no")
    with pytest.raises(Exception):
        obj.set("a string", "region", "oslo", "no")
