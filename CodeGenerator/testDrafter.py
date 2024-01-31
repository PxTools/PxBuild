from SpecReader import SpecReader

intro_fstring = """\
import pytest
from pxbuild.models.output.pxfile.keywords.{kw.module_name} import {my_class}
"""

set_valid_fstring = """
def test{my_class}_set_valid():
    obj = {my_class}()
    assert not obj.has_value()
    obj.set({good_value})
    assert obj.has_value()
    assert obj.get_value() == {good_value}
"""

set_valid_with_keypart_fstring = """
def test{my_class}_set_valid():
    obj = {my_class}()
    assert not obj.has_value({keypart})
    obj.set({good_value},{keypart})
    assert obj.has_value({keypart})
    assert obj.get_value({keypart}) == {good_value}
"""

language_management_with_keypart_fstring = """
def test{my_class}_used_languages():
    obj = {my_class}()
    obj.set({good_value},{keypart})
    assert "no" in obj.get_used_languages()

def test{my_class}_reset_language():
    obj = {my_class}()
    obj.set({good_value},{keypart_no_lang})
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)
    obj.reset_language_none_to("no")
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()

"""

set_invalid_fstring = """
def test{my_class}_set_invalid_raises():
    obj = {my_class}()
    with pytest.raises(Exception):
       obj.set({bad_value})
"""

set_invalid_with_keypart_fstring = """
def test{my_class}_set_invalid_raises():
    obj = {my_class}()
    with pytest.raises(Exception):
       obj.set({bad_value},{keypart})
"""

duplicate_set_fstring = """
def test{my_class}_duplicate_set_raises():
    obj = {my_class}()
    obj.set({good_value})
    with pytest.raises(Exception):
        obj.set({good_value})
"""

duplicate_set_with_keypart_fstring = """
def test{my_class}_duplicate_set_raises():
    obj = {my_class}()
    obj.set({good_value},{keypart})
    with pytest.raises(Exception):
        obj.set({good_value},{keypart})
"""

hack_forcing_error_multi_with_keypart_fstring = """
def test{my_class}_hack_multi_duplicate_set_raises():
    obj = {my_class}()
    obj.set({good_value},{keypart})
    #reseting counter to create error
    obj.occurence_counter=0
    with pytest.raises(Exception) as err_mess:
        obj.set({good_value},{keypart})
    assert str(err_mess.value).startswith("{kw.keyword}:")
"""

######################################################################################
def get_keypart(subkeys: str) -> str:
    my_out = '"no"'
    subpart = get_keypart_no_lang(subkeys)
    if subpart:
        my_out = subpart + "," + my_out
    return my_out


def get_keypart_no_lang(subkeys: str) -> str:
    my_out = ""
    if subkeys in ["variable:str", "variable:str=None"]:
        my_out = '"region"'
    elif subkeys in ["content:str=None"]:
        my_out = '"persons"'
    elif subkeys in ["variable:str,value:str", "variable:str, value:str", "variable:str=None, value:str=None"]:
        my_out = '"region","oslo"'
    elif subkeys in ["values:list[str]", "values:list[str]=None"]:
        my_out = '["male","oslo"]'
    return my_out


def test_lang_string_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = '"a string"'
    if kw.keyword == "CFPRICES":
        good_value = '"F"'
    elif kw.keyword == "KEYS":
        good_value = '"CODES"'
    elif kw.keyword == "STOCKFA":
        good_value = '"F"'

    filehandle.write(intro_fstring.format(**locals()))
    keypart = get_keypart(kw.subkeys_raw.strip())
    keypart_no_lang = get_keypart_no_lang(kw.subkeys_raw.strip())

    filehandle.write(set_valid_with_keypart_fstring.format(**locals()))

    filehandle.write(language_management_with_keypart_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_with_keypart_fstring.format(**locals()))
    else:
        filehandle.write(hack_forcing_error_multi_with_keypart_fstring.format(**locals()))


def test_lang_stringlist_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = '["a string"]'

    filehandle.write(intro_fstring.format(**locals()))
    keypart = get_keypart(kw.subkeys_raw.strip())
    keypart_no_lang = get_keypart_no_lang(kw.subkeys_raw.strip())

    filehandle.write(set_valid_with_keypart_fstring.format(**locals()))

    filehandle.write(language_management_with_keypart_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_with_keypart_fstring.format(**locals()))
    else:
        filehandle.write(hack_forcing_error_multi_with_keypart_fstring.format(**locals()))


#####


def test_scalar_string_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = '"a string"'
    if kw.keyword == "AXIS-VERSION":
        good_value = '"2222"'
    elif kw.keyword == "LANGUAGE":
        good_value = '"en"'

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    if not good_value == '"a string"':
        bad_value = '"bad_string"'
        # if kw.keyword ..
        filehandle.write(set_invalid_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_fstring.format(**locals()))


######


def test_scalar_stringlist_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = '["a string"]'
    if kw.keyword == "LANGUAGES":
        good_value = '["en"]'

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    if not good_value == '["a string"]':
        bad_value = '["bad_string"]'
        # if kw.keyword ..
        filehandle.write(set_invalid_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_fstring.format(**locals()))


#####


def test_scalar_bool_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = True

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_fstring.format(**locals()))


####
def test_lang_bool_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = True

    filehandle.write(intro_fstring.format(**locals()))

    keypart = get_keypart(kw.subkeys_raw.strip())
    keypart_no_lang = get_keypart_no_lang(kw.subkeys_raw.strip())

    filehandle.write(set_valid_with_keypart_fstring.format(**locals()))
    filehandle.write(language_management_with_keypart_fstring.format(**locals()))
    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_with_keypart_fstring.format(**locals()))


####


def test_with_keypart_int_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = 1
    keypart = get_keypart(kw.subkeys_raw.strip())
    keypart_no_lang = get_keypart_no_lang(kw.subkeys_raw.strip())

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_with_keypart_fstring.format(**locals()))
    if "in_range" in "".join(kw.linevalidate):
        bad_value = 666
        filehandle.write(set_invalid_fstring.format(**locals()))

    filehandle.write(language_management_with_keypart_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_with_keypart_fstring.format(**locals()))


def test_scalar_int_writer(kw, filehandle) -> None:
    my_class = kw.classnames["This"]

    good_value = 1

    filehandle.write(intro_fstring.format(**locals()))
    filehandle.write(set_valid_fstring.format(**locals()))
    if "in_range" in kw.linevalidate:
        bad_value = 666
        filehandle.write(set_invalid_fstring.format(**locals()))

    if not kw.is_duplicate_keypart_allowed:
        filehandle.write(duplicate_set_fstring.format(**locals()))


###################################################################################

my_spec = SpecReader()
dir_string = "../tests/model/keywords/test"
# make test_<Keyword classes>.py
for kw in my_spec.data:
    if kw.keyword in ["DATA", "TIMEVAL", "ATTRIBUTES", "HIERARCHYLEVELSOPEN", "HIERARCHYLEVELS", "HIERARCHIES"]:
        print(f"Skipping {kw.keyword}.")
        continue

    if not kw.has_lang:
        if not kw.subkeys_raw:
            if kw.px_valuetype in ["_PxString"]:
                with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                    test_scalar_string_writer(kw, classPy)

            elif kw.px_valuetype == "_PxBool":
                with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                    test_scalar_bool_writer(kw, classPy)
            elif kw.px_valuetype == "_PxInt":
                with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                    test_scalar_int_writer(kw, classPy)
            elif kw.px_valuetype == "_PxStringList":
                with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                    test_scalar_stringlist_writer(kw, classPy)
            else:
                print(f"miss {kw.keyword}")
        else:
            print(f"subkeys so miss {kw.keyword}")
    else:
        if kw.px_valuetype in ["_PxString"]:
            with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                test_lang_string_writer(kw, classPy)
        elif kw.px_valuetype == "_PxBool":
            with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                test_lang_bool_writer(kw, classPy)
        elif kw.px_valuetype == "_PxInt":
            with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                test_with_keypart_int_writer(kw, classPy)
        elif kw.px_valuetype == "_PxStringList":
            with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig", newline="\n") as classPy:
                test_lang_stringlist_writer(kw, classPy)


print("Done")
