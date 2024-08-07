﻿import pytest
from pxbuild.models.output.pxfile.keywords._seasadj import _Seasadj


def test_seasadj_set_valid():
    obj = _Seasadj()
    assert not obj.has_value("persons", "no")
    obj.set(True, "persons", "no")
    assert obj.has_value("persons", "no")
    assert obj.get_value("persons", "no")


def test_seasadj_used_languages():
    obj = _Seasadj()
    obj.set(True, "persons", "no")
    assert "no" in obj.get_used_languages()


def test_seasadj_reset_language():
    obj = _Seasadj()
    obj.set(True, "persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert None not in obj.get_used_languages()
    assert "no" in obj.get_used_languages()


def test_seasadj_duplicate_set_raises():
    obj = _Seasadj()
    obj.set(True, "persons", "no")
    with pytest.raises(ValueError):
        obj.set(True, "persons", "no")
