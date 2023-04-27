import pytest
from pxtool.model.keywords._subject_code import _SubjectCode
    
def test_SubjectCode_set_valid():
    obj = _SubjectCode("SUBJECT-CODE")
    obj.set("a string")
    assert obj.get_value() == "a string"
    
def test_SubjectCode_duplicate_set_raises():
    obj = _SubjectCode("SUBJECT-CODE")
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")
