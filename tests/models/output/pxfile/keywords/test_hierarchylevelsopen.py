import pytest
from pxbuild.models.output.pxfile.keywords._hierarchylevelsopen import _Hierarchylevelsopen


def test_Hierarchylevelsopen_set_valid():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region", "no")
    assert obj.get_value("region", "no") == 3


def test_Hierarchylevelsopen_used_languages():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region", "no")
    assert "no" in obj.get_used_languages()


def test_Hierarchylevelsopen_reset_language():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_Hierarchylevelsopen_duplicate_set_raises():
    obj = _Hierarchylevelsopen()
    obj.set(3, "region", "no")
    with pytest.raises(Exception):
        obj.set(3, "region", "no")
