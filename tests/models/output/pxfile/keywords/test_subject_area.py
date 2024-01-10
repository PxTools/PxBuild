import pytest
from pxbuild.models.output.pxfile.keywords._subject_area import _SubjectArea
    
def test_SubjectArea_set_valid():
    obj = _SubjectArea()
    assert not obj.has_value("no")    
    obj.set("a string","no")
    assert obj.has_value("no")    
    assert obj.get_value("no") == "a string"
    
def test_SubjectArea_used_languages():
    obj = _SubjectArea()
    obj.set("a string","no")
    assert "no" in obj.get_used_languages()

def test_SubjectArea_reset_language():
    obj = _SubjectArea()
    obj.set("a string",)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_SubjectArea_duplicate_set_raises():
    obj = _SubjectArea()
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
