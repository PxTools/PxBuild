import pytest
from pxbuild.models.output.pxfile.keywords._valuenotex import _Valuenotex


def test_valuenotex_set_valid():
    obj = _Valuenotex()
    assert not obj.has_value("region", "oslo", "no")
    obj.set("a string", "region", "oslo", "no")
    assert obj.has_value("region", "oslo", "no")
    assert obj.get_value("region", "oslo", "no") == "a string"


def test_valuenotex_used_languages():
    obj = _Valuenotex()
    obj.set("a string", "region", "oslo", "no")
    assert "no" in obj.get_used_languages()


def test_valuenotex_reset_language():
    obj = _Valuenotex()
    obj.set("a string", "region", "oslo")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_valuenotex_hack_multi_duplicate_set_raises():
    obj = _Valuenotex()
    obj.set("a string", "region", "oslo", "no")
    # reseting counter to create error
    obj.occurence_counter = 0
    with pytest.raises(Exception) as err_mess:
        obj.set("a string", "region", "oslo", "no")
    assert str(err_mess.value).startswith("VALUENOTEX:")
