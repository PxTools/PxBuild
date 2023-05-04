import pytest
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeValuesMulti, _KeytypeValuesLangMulti, _KeytypeVariableValueLangMulti, _KeytypeVariableLangMulti, _KeytypeLang,_KeytypeVariableLang,_KeytypeContentLang, _KeytypeVariableValueLang,_KeytypeVariableValue
def test_eq_returns_false():

    my_str = "no"
    my_key = _KeytypeLang("no")
    assert not my_key == my_str
    
    my_key = _KeytypeVariableLang("region","no")
    assert not my_key == my_str
    
    #TODO: included for coverage, should remove method instead?
    my_key.reset_lang_none_to("sv")
    
    
    my_key = _KeytypeContentLang("region","no")
    assert not my_key == my_str
    
    #TODO: included for coverage, should remove method instead?
    str_mess= my_key.to_str_message()
    my_key.reset_lang_none_to("sv")
    
    my_key = _KeytypeVariableValueLang("region","oslo","no")
    assert not my_key == my_str
    my_key.reset_lang_none_to("sv")


    my_key = _KeytypeVariableValue("region","oslo")
    assert not my_key == my_str
   
    my_key = _KeytypeVariableLangMulti("region","no",1)
    assert not my_key == my_str

    my_key.reset_lang_none_to("sv")

    my_key = _KeytypeVariableValueLangMulti("region","oslo","no",1)
    assert not my_key == my_str
    my_key.reset_lang_none_to("sv")

    my_key = _KeytypeValuesLangMulti(["kongsvinger","oslo"],"no",1)
    assert not my_key == my_str
    my_key.reset_lang_none_to("sv")

    my_key = _KeytypeValuesMulti(["kongsvinger","oslo"],1)
    assert not my_key == my_str
