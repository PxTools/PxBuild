﻿import pytest
from pxbuild.models.output.pxfile.keywords._map import _Map


def test_map_set_valid():
    obj = _Map()
    assert not obj.has_value("region", "no")
    obj.set("a string", "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == "a string"


def test_map_used_languages():
    obj = _Map()
    obj.set("a string", "region", "no")
    assert "no" in obj.get_used_languages()


def test_map_reset_language():
    obj = _Map()
    obj.set("a string", "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_map_duplicate_set_raises():
    obj = _Map()
    obj.set("a string", "region", "no")
    with pytest.raises(ValueError):
        obj.set("a string", "region", "no")
