﻿import pytest
from pxbuild.models.output.pxfile.keywords._last_updated import _LastUpdated


def test_lastupdated_set_valid():
    obj = _LastUpdated()
    assert not obj.has_value("persons", "no")
    obj.set("a string", "persons", "no")
    assert obj.has_value("persons", "no")
    assert obj.get_value("persons", "no") == "a string"


def test_lastupdated_used_languages():
    obj = _LastUpdated()
    obj.set("a string", "persons", "no")
    assert "no" in obj.get_used_languages()


def test_lastupdated_reset_language():
    obj = _LastUpdated()
    obj.set("a string", "persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_lastupdated_duplicate_set_raises():
    obj = _LastUpdated()
    obj.set("a string", "persons", "no")
    with pytest.raises(ValueError):
        obj.set("a string", "persons", "no")
