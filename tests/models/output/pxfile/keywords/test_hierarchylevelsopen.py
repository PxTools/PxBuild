import pytest
from pxbuild.models.output.pxfile.keywords._hierarchylevelsopen import _Hierarchylevelsopen


def test_hierarchylevelsopen_set_valid():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region", "no")
    assert obj.get_value("region", "no") == 3


def test_hierarchylevelsopen_used_languages():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region", "no")
    assert "no" in obj.get_used_languages()


def test_hierarchylevelsopen_reset_language():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_hierarchylevelsopen_duplicate_set_raises():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region", "no")
    with pytest.raises(ValueError):
        obj.set(3, "region", "no")
