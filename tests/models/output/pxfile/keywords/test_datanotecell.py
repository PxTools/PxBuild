import pytest
from pxbuild.models.output.pxfile.keywords._datanotecell import _Datanotecell


def test_Datanotecell_set_valid():
    obj = _Datanotecell()
    assert not obj.has_value(["male", "oslo"], "no")
    obj.set("a string", ["male", "oslo"], "no")
    assert obj.has_value(["male", "oslo"], "no")
    assert obj.get_value(["male", "oslo"], "no") == "a string"


def test_Datanotecell_used_languages():
    obj = _Datanotecell()
    obj.set("a string", ["male", "oslo"], "no")
    assert "no" in obj.get_used_languages()


def test_Datanotecell_reset_language():
    obj = _Datanotecell()
    obj.set("a string", ["male", "oslo"])
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_Datanotecell_hack_multi_duplicate_set_raises():
    obj = _Datanotecell()
    obj.set("a string", ["male", "oslo"], "no")
    # reseting counter to create error
    obj.occurence_counter = 0
    with pytest.raises(Exception) as err_mess:
        obj.set("a string", ["male", "oslo"], "no")
    assert str(err_mess.value).startswith("DATANOTECELL:")
