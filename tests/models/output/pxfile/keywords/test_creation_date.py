﻿import pytest
from pxbuild.models.output.pxfile.keywords._creation_date import _CreationDate


def test_creationdate_set_valid():
    obj = _CreationDate()
    assert not obj.has_value()
    obj.set("a string")
    assert obj.has_value()
    assert obj.get_value() == "a string"


def test_creationdate_duplicate_set_raises():
    obj = _CreationDate()
    obj.set("a string")
    with pytest.raises(ValueError):
        obj.set("a string")
