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

    my_key = _KeytypeValuesMulti(["kongsvinger","oslo"],1)
    assert not my_key == my_str


def test_KeytypeValuesLangMulti():
    my_key = _KeytypeValuesLangMulti(["kongsvinger","oslo"],"no",1)
    assert not my_key == "astring"
    my_key2 = _KeytypeValuesLangMulti(["kongsvinger","oslo"],"no",1)
    assert my_key == my_key2
    assert hash(my_key) == hash(my_key2)
    my_key3 = _KeytypeValuesLangMulti(["kongsvinger","Oslo"],"no",1)
    assert not my_key == my_key3
    
    my_key4 = _KeytypeValuesLangMulti(["kongsvinger","Oslo"],None,1)
    my_key5  = my_key4.reset_lang_none_to("sv")
    assert isinstance(my_key5, _KeytypeValuesLangMulti)
    my_key6  = my_key5.reset_lang_none_to("sv")


def test_lab_test():
    my_key = _KeytypeValuesLangMulti(["kongsvinger","oslo"],"no",1)
    my_key2 = _KeytypeLang("no");

    assert isinstance(my_key2, _KeytypeLang)
    assert isinstance(my_key, _KeytypeLang)
    assert not type(my_key) == type(my_key2)

def test_lab_test2():
    my_key4 = _KeytypeValuesLangMulti(["kongsvinger","oslo"],"no",1)
    my_key2 = _KeytypeLang("no");

    assert not my_key2 == my_key4
    assert not my_key4 == my_key2


def test_lab_test3():
    my_key2 = _KeytypeLang("no");
    my_key3 = _KeytypeLang("no");
    assert my_key2 == my_key3
    