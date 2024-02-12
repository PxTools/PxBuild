from typing import List

from SpecReader import SpecReader
from test_templates import TstTemplates


def get_keypart(subkeys: str) -> str:
    my_out = '"no"'
    subpart = get_keypart_no_lang(subkeys)
    if subpart:
        my_out = subpart + ", " + my_out
    return my_out


def get_keypart_no_lang(subkeys: str) -> str:
    my_out = ""
    if subkeys in ["variable:str", "variable:str=None"]:
        my_out = '"region"'
    elif subkeys in ["content:str=None"]:
        my_out = '"persons"'
    elif subkeys in ["variable:str,value:str", "variable:str, value:str", "variable:str=None, value:str=None"]:
        my_out = '"region", "oslo"'
    elif subkeys in ["values:list[str]", "values:list[str]=None"]:
        my_out = '["male", "oslo"]'
    return my_out


def test_lang_string_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "keypart": get_keypart(kw.subkeys_raw.strip()),
        "keypart_no_lang": get_keypart_no_lang(kw.subkeys_raw.strip()),
    }

    if kw.keyword == "CFPRICES":
        data["good_value"] = '"F"'
    elif kw.keyword == "KEYS":
        data["good_value"] = '"CODES"'
    elif kw.keyword == "STOCKFA":
        data["good_value"] = '"F"'
    else:
        data["good_value"] = '"a string"'

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_with_key.render(data))

    if data["keypart_no_lang"]:
        my_out.append(my_templates.language_management_with_subkey.render(data))
    else:
        my_out.append(my_templates.language_management_no_subkey.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_with_key.render(data))
    else:
        data["keyword"] = kw.keyword
        my_out.append(my_templates.hack_forcing_error_multi_raises_with_key.render(data))
    return my_out


def test_lang_stringlist_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "keypart": get_keypart(kw.subkeys_raw.strip()),
        "keypart_no_lang": get_keypart_no_lang(kw.subkeys_raw.strip()),
        "good_value": '["a string"]',
    }

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_with_key.render(data))

    if data["keypart_no_lang"]:
        my_out.append(my_templates.language_management_with_subkey.render(data))
    else:
        my_out.append(my_templates.language_management_no_subkey.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_with_key.render(data))
    else:
        data["keyword"] = kw.keyword
        my_out.append(my_templates.hack_forcing_error_multi_raises_with_key.render(data))
    return my_out


#####


def test_scalar_string_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
    }

    if kw.keyword == "AXIS-VERSION":
        data["good_value"] = '"2222"'
        data["bad_value"] = '"bad_string"'
    elif kw.keyword == "LANGUAGE":
        data["good_value"] = '"en"'
        data["bad_value"] = '"bad_string"'
    else:
        data["good_value"] = '"a string"'

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_keyless.render(data))

    if "bad_value" in data:
        my_out.append(my_templates.set_invalid_keyless.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_keyless.render(data))

    return my_out


######


def test_scalar_stringlist_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "good_value": '["a string"]',
    }
    if kw.keyword == "LANGUAGES":
        data["good_value"] = '["en"]'
        data["bad_value"] = '["bad_string"]'

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_keyless.render(data))

    if "bad_value" in data:
        my_out.append(my_templates.set_invalid_keyless.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_keyless.render(data))

    return my_out


#####


def test_scalar_bool_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "good_value": True,
    }

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_bool_keyless.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_keyless.render(data))

    return my_out


####
def test_lang_bool_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "keypart": get_keypart(kw.subkeys_raw.strip()),
        "keypart_no_lang": get_keypart_no_lang(kw.subkeys_raw.strip()),
        "good_value": True,
    }

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_bool_with_key.render(data))

    if data["keypart_no_lang"]:
        my_out.append(my_templates.language_management_with_subkey.render(data))
    else:
        my_out.append(my_templates.language_management_no_subkey.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_with_key.render(data))
    return my_out


####


def test_with_keypart_int_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "keypart": get_keypart(kw.subkeys_raw.strip()),
        "keypart_no_lang": get_keypart_no_lang(kw.subkeys_raw.strip()),
        "good_value": 1,
    }

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_with_key.render(data))

    if "in_range" in "".join(kw.linevalidate):
        data["bad_value"] = 667
        my_out.append(my_templates.set_invalid_with_key.render(data))

    if data["keypart_no_lang"]:
        my_out.append(my_templates.language_management_with_subkey.render(data))
    else:
        my_out.append(my_templates.language_management_no_subkey.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_with_key.render(data))
    return my_out


def test_scalar_int_writer(kw) -> List[str]:
    # Data to be rendered in the templates
    data = {
        "object_module_name": kw.module_name,
        "object_class": kw.classnames["This"],
        "test_class_lower": kw.classnames["This"].lower(),
        "good_value": 1,
    }

    # Render the template with data
    my_out: List[str] = [my_templates.intro.render(data)]
    my_out.append(my_templates.set_valid_keyless.render(data))

    if "in_range" in kw.linevalidate:
        data["bad_value"] = 666
        my_out.append(my_templates.set_invalid_keyless.render(data))

    if not kw.is_duplicate_keypart_allowed:
        my_out.append(my_templates.duplicate_set_raises_keyless.render(data))

    return my_out


###################################################################################

my_spec = SpecReader()
dir_string = "../tests/models/output/pxfile/keywords/test"

# Create an environment instance

my_templates: TstTemplates = TstTemplates()


# make test_<Keyword classes>.py
for kw in my_spec.data:
    if kw.keyword in ["DATA", "TIMEVAL", "ATTRIBUTES", "HIERARCHYLEVELSOPEN", "HIERARCHYLEVELS", "HIERARCHIES"]:
        print(f"Skipping {kw.keyword}.")
        continue

    my_out: str = ""
    if not kw.has_lang:
        if not kw.subkeys_raw:
            if kw.px_valuetype in ["_PxString"]:
                my_out = test_scalar_string_writer(kw)
            elif kw.px_valuetype == "_PxBool":
                my_out = test_scalar_bool_writer(kw)
            elif kw.px_valuetype == "_PxInt":
                my_out = test_scalar_int_writer(kw)
            elif kw.px_valuetype == "_PxStringList":
                my_out = test_scalar_stringlist_writer(kw)
            else:
                print(f"Error: unknown px_valuetype {kw.px_valuetype}, for {kw.keyword}")
        else:
            print(f"subkeys so miss {kw.keyword}")
    else:
        if kw.px_valuetype in ["_PxString"]:
            my_out = test_lang_string_writer(kw)
        elif kw.px_valuetype == "_PxBool":
            my_out = test_lang_bool_writer(kw)
        elif kw.px_valuetype == "_PxInt":
            my_out = test_with_keypart_int_writer(kw)
        elif kw.px_valuetype == "_PxStringList":
            my_out = test_lang_stringlist_writer(kw)
        else:
            print(f" kw.has_lang.  miss {kw.keyword}")

    if my_out:
        my_out2 = "\n\n\n".join(my_out).rstrip() + "\n"
        with open(dir_string + kw.module_name + ".py", "wt", encoding="utf-8-sig") as class_py:
            class_py.write(my_out2)


print("Done")
