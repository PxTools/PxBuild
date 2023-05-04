import pytest
from pxtool.model.keywords._note import _Note
    
def test_Note_set_valid():
    obj = _Note()
    obj.set("a string","region","no")
    assert obj.get_value("region","no") == "a string"
    
def test_Note_used_languages():
    obj = _Note()
    obj.set("a string","region","no")
    assert "no" in obj.get_used_languages()

def test_Note_reset_language():
    obj = _Note()
    obj.set("a string","region")
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Note_hack_multi_duplicate_set_raises():
    obj = _Note()
    obj.set("a string","region","no")
    #reseting counter to create error
    obj.occurence_counter=0
    with pytest.raises(Exception) as err_mess:
        obj.set("a string","region","no")
    assert str(err_mess.value).startswith("NOTE:")
