import pytest
from pxbuild.models.output.pxfile.keywords._cellnote import _Cellnote


def test_cellnote_set_valid():
    obj = _Cellnote()
    assert not obj.has_value(["male", "oslo"], "no")
    obj.set("a string", ["male", "oslo"], "no")
    assert obj.has_value(["male", "oslo"], "no")
    assert obj.get_value(["male", "oslo"], "no") == "a string"


def test_cellnote_used_languages():
    obj = _Cellnote()
    obj.set("a string", ["male", "oslo"], "no")
    assert "no" in obj.get_used_languages()


def test_cellnote_reset_language():
    obj = _Cellnote()
    obj.set("a string", ["male", "oslo"])
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_cellnote_hack_multi_duplicate_set_raises():
    obj = _Cellnote()
    obj.set("a string", ["male", "oslo"], "no")
    # reseting counter to create error
    obj.occurence_counter = 0
    with pytest.raises(Exception) as err_mess:
        obj.set("a string", ["male", "oslo"], "no")
    assert str(err_mess.value).startswith("CELLNOTE:")
