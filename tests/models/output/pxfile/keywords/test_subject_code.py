import pytest
from pxbuild.models.output.pxfile.keywords._subject_code import _SubjectCode


def test_subjectcode_set_valid():
    obj = _SubjectCode()
    assert not obj.has_value()
    obj.set("a string")
    assert obj.has_value()
    assert obj.get_value() == "a string"


def test_subjectcode_duplicate_set_raises():
    obj = _SubjectCode()
    obj.set("a string")
    with pytest.raises(ValueError):
        obj.set("a string")
