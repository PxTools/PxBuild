﻿import pytest
from pxbuild.models.output.pxfile.keywords._cellnotex import _Cellnotex


def test_cellnotex_set_valid():
    obj = _Cellnotex()
    assert not obj.has_value(["male", "oslo"], "no")
    obj.set("a string", ["male", "oslo"], "no")
    assert obj.has_value(["male", "oslo"], "no")
    assert obj.get_value(["male", "oslo"], "no") == "a string"


def test_cellnotex_used_languages():
    obj = _Cellnotex()
    obj.set("a string", ["male", "oslo"], "no")
    assert "no" in obj.get_used_languages()


def test_cellnotex_reset_language():
    obj = _Cellnotex()
    obj.set("a string", ["male", "oslo"])
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_cellnotex_hack_multi_duplicate_set_raises():
    obj = _Cellnotex()
    obj.set("a string", ["male", "oslo"], "no")
    # reseting counter to create error
    obj.occurence_counter = 0
    with pytest.raises(ValueError) as err_mess:
        obj.set("a string", ["male", "oslo"], "no")
    assert str(err_mess.value).startswith("CELLNOTEX:")
