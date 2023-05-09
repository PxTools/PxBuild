﻿import pytest
from pxtool.model.keywords._attribute_text import _AttributeText
    
def test_AttributeText_set_valid():
    obj = _AttributeText()
    obj.set(["a string"],"no")
    assert obj.get_value("no") == ["a string"]
    
def test_AttributeText_used_languages():
    obj = _AttributeText()
    obj.set(["a string"],"no")
    assert "no" in obj.get_used_languages()

def test_AttributeText_reset_language():
    obj = _AttributeText()
    obj.set(["a string"],)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_AttributeText_duplicate_set_raises():
    obj = _AttributeText()
    obj.set(["a string"],"no")
    with pytest.raises(Exception):
        obj.set(["a string"],"no")