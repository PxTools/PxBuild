import pytest
from pxtool.model.keywords._subject_area import _SubjectArea
    
def test_SubjectArea_set_valid():
    obj = _SubjectArea("SUBJECT-AREA")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_SubjectArea_duplicate_set_raises():
    obj = _SubjectArea("SUBJECT-AREA")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
