import pytest
from pxbuild.models.output.pxfile.keywords._timeval import _Timeval


def test_timeval_set_valid():
    obj = _Timeval()

    obj.set("A1", ["1994", "1995", "1996"], "time", "no")
    assert obj.get_value("time", "no") == ("A1", ["1994", "1995", "1996"])


def test_timeval_used_languages():
    obj = _Timeval()
    obj.set("A1", ["1994", "1995", "1996"], "time", "no")
    assert "no" in obj.get_used_languages()


def test_timeval_reset_language():
    obj = _Timeval()
    obj.set("A1", ["1994", "1995", "1996"], "time")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_timeval_duplicate_set_raises():
    obj = _Timeval()
    obj.set("A1", ["1994", "1995", "1996"], "time", "no")
    with pytest.raises(ValueError):
        obj.set("A1", ["1994", "1995", "1996"], "time", "no")
