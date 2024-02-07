import pytest
from pxbuild.models.output.pxfile.keywords._notex import _Notex


def test_notex_set_valid():
    obj = _Notex()
    assert not obj.has_value("region", "no")
    obj.set("a string", "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == "a string"


def test_notex_used_languages():
    obj = _Notex()
    obj.set("a string", "region", "no")
    assert "no" in obj.get_used_languages()


def test_notex_reset_language():
    obj = _Notex()
    obj.set("a string", "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_notex_hack_multi_duplicate_set_raises():
    obj = _Notex()
    obj.set("a string", "region", "no")
    # reseting counter to create error
    obj.occurence_counter = 0
    with pytest.raises(ValueError) as err_mess:
        obj.set("a string", "region", "no")
    assert str(err_mess.value).startswith("NOTEX:")
