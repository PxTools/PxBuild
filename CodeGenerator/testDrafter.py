from SpecReader import SpecReader

intro_fstring ="""\
import pytest
from pxtool.model.keywords.{kw.module_name} import {my_class}
"""

set_valid_fstring="""    
def test{my_class}_set_valid():
    obj = {my_class}("{kw.keyword}")
    obj.set({good_value})
    assert obj.get_value() == {good_value}
"""

set_valid_with_lang_fstring="""    
def test{my_class}_set_valid():
    obj = {my_class}("{kw.keyword}")
    obj.set({good_value},"no")
    assert obj.get_value("no") == {good_value}
"""

set_invalid_fstring="""    
def test{my_class}_set_invalid_raises():
    obj = {my_class}("{kw.keyword}")
    with pytest.raises(Exception):
       obj.set({bad_value})
"""

duplicate_set_fstring="""    
def test{my_class}_duplicate_set_raises():
    obj = {my_class}("{kw.keyword}")
    obj.set({good_value})
    with pytest.raises(Exception):
        obj.set({good_value})
"""

duplicate_set_with_lang_fstring="""    
def test{my_class}_duplicate_set_raises():
    obj = {my_class}("{kw.keyword}")
    obj.set({good_value},"no")
    with pytest.raises(Exception):
        obj.set({good_value},"no")
"""



######################################################################################

def test_lang_string_writer(kw, filehandle) -> None:
    my_class = kw.classnames['This']

    good_value= "\"a string\""

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_with_lang_fstring.format(**locals()))
    
    if(not kw.is_duplicate_keypart_allowed):
        filehandle.write(duplicate_set_with_lang_fstring.format(**locals()))

#####

def test_scalar_string_writer(kw, filehandle) -> None:
    my_class = kw.classnames['This']

    good_value= "\"a string\""
    if(kw.keyword == "AXIS-VERSION"):
        good_value= "\"2222\""
    elif(kw.keyword == "LANGUAGE"):
        good_value= "\"en\"" 

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    if(not good_value == "\"a string\""):
        bad_value="\"bad_string\""
        #if kw.keyword ..
        filehandle.write(set_invalid_fstring.format(**locals()))

    if(not kw.is_duplicate_keypart_allowed):
        filehandle.write(duplicate_set_fstring.format(**locals()))

######

def test_scalar_stringlist_writer(kw, filehandle) -> None:
    my_class = kw.classnames['This']

    good_value= "[\"a string\"]"
    if(kw.keyword == "LANGUAGES"):
        good_value= "[\"en\"]" 

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    if(not good_value == "[\"a string\"]"):
        bad_value="[\"bad_string\"]"
        #if kw.keyword ..
        filehandle.write(set_invalid_fstring.format(**locals()))

    if(not kw.is_duplicate_keypart_allowed):
        filehandle.write(duplicate_set_fstring.format(**locals()))

#####        

def test_scalar_bool_writer(kw, filehandle) -> None:
    my_class = kw.classnames['This']

    good_value = True

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    
    if(not kw.is_duplicate_keypart_allowed):
        filehandle.write(duplicate_set_fstring.format(**locals()))

####

def test_scalar_int_writer(kw, filehandle) -> None:
    my_class = kw.classnames['This']

    good_value= 1

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    if('in_range' in kw.linevalidate):
        bad_value=666
        filehandle.write(set_invalid_fstring.format(**locals()))

    if(not kw.is_duplicate_keypart_allowed):
        filehandle.write(duplicate_set_fstring.format(**locals()))

###################################################################################

my_spec= SpecReader()

# make test_<Keyword classes>.py
for kw in my_spec.data:
    if(not kw.has_lang):
      if(not kw.subkeys_raw):
        if(kw.px_valuetype in ["_PxString"] ):
            with open("../tests/keywords/test"+kw.module_name+".py", "wt",encoding="utf-8-sig", newline="\n" ) as classPy:
               test_scalar_string_writer(kw,classPy)
               
        elif(kw.px_valuetype == "_PxBool"):
            with open("../tests/keywords/test"+kw.module_name+".py", "wt",encoding="utf-8-sig", newline="\n" ) as classPy:
               test_scalar_bool_writer(kw,classPy)
        elif(kw.px_valuetype == "_PxInt"):
            with open("../tests/keywords/test"+kw.module_name+".py", "wt",encoding="utf-8-sig", newline="\n" ) as classPy:
               test_scalar_int_writer(kw,classPy)
        elif(kw.px_valuetype == "_PxStringList"):
            with open("../tests/keywords/test"+kw.module_name+".py", "wt",encoding="utf-8-sig", newline="\n" ) as classPy:
               test_scalar_stringlist_writer(kw,classPy)
        else:
            print(f"miss {kw.keyword}")
      else:
        print(f"subkeys so miss {kw.keyword}")
    else:
      if(not kw.subkeys_raw):
          if(kw.px_valuetype in ["_PxString"] ):
            with open("../tests/keywords/test"+kw.module_name+".py", "wt",encoding="utf-8-sig", newline="\n" ) as classPy:
               test_lang_string_writer(kw,classPy)

print("Done")









