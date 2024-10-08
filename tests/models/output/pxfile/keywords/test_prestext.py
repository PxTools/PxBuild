﻿import pytest
from pxbuild.models.output.pxfile.keywords._prestext import _Prestext


def test_prestext_set_valid():
    obj = _Prestext()
    assert not obj.has_value("region", "no")
    obj.set(1, "region", "no")
    assert obj.has_value("region", "no")
    assert obj.get_value("region", "no") == 1


def test_prestext_set_invalid_raises():
    obj = _Prestext()
    with pytest.raises(ValueError):
        obj.set(667, "region", "no")


def test_prestext_used_languages():
    obj = _Prestext()
    obj.set(1, "region", "no")
    assert "no" in obj.get_used_languages()


def test_prestext_reset_language():
    obj = _Prestext()
    obj.set(1, "region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_prestext_duplicate_set_raises():
    obj = _Prestext()
    obj.set(1, "region", "no")
    with pytest.raises(ValueError):
        obj.set(1, "region", "no")
