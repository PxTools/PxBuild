﻿import pytest
from pxtool.model.keywords._cfprices import _Cfprices
    
def test_Cfprices_set_valid():
    obj = _Cfprices()
    obj.set("F","persons","no")
    assert obj.get_value("persons","no") == "F"
    
def test_Cfprices_used_languages():
    obj = _Cfprices()
    obj.set("F","persons","no")
    assert "no" in obj.get_used_languages()

def test_Cfprices_reset_language():
    obj = _Cfprices()
    obj.set("F","persons")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Cfprices_duplicate_set_raises():
    obj = _Cfprices()
    obj.set("F","persons","no")
    with pytest.raises(Exception):
        obj.set("F","persons","no")