import pytest
from pxbuild.models.output.pxfile.keywords._hierarchynames import _Hierarchynames


def test_hierarchynames_set_valid():
    obj = _Hierarchynames()
    assert not obj.has_value("region", "no")
    obj.set(["a string"], "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == ["a string"]


def test_hierarchynames_used_languages():
    obj = _Hierarchynames()
    obj.set(["a string"], "region", "no")
    assert "no" in obj.get_used_languages()


def test_hierarchynames_reset_language():
    obj = _Hierarchynames()
    obj.set(["a string"], "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_hierarchynames_duplicate_set_raises():
    obj = _Hierarchynames()
    obj.set(["a string"], "region", "no")
    with pytest.raises(ValueError):
        obj.set(["a string"], "region", "no")
