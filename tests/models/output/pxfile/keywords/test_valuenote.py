import pytest
from pxbuild.models.output.pxfile.keywords._valuenote import _Valuenote


def test_valuenote_set_valid():
    obj = _Valuenote()
    assert not obj.has_value("region", "oslo", "no")
    obj.set("a string", "region", "oslo", "no")
    assert obj.has_value("region", "oslo", "no")
    assert obj.get_value("region", "oslo", "no") == "a string"


def test_valuenote_used_languages():
    obj = _Valuenote()
    obj.set("a string", "region", "oslo", "no")
    assert "no" in obj.get_used_languages()


def test_valuenote_reset_language():
    obj = _Valuenote()
    obj.set("a string", "region", "oslo")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_valuenote_hack_multi_duplicate_set_raises():
    obj = _Valuenote()
    obj.set("a string", "region", "oslo", "no")
    # reseting counter to create error
    obj.occurence_counter = 0
    with pytest.raises(Exception) as err_mess:
        obj.set("a string", "region", "oslo", "no")
    assert str(err_mess.value).startswith("VALUENOTE:")
