import pytest
from pxbuild.models.output.pxfile.util._px_super import _PxSingle, _PxValueByKey
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeLang


def test_super():
    my_str = "a string"

    my_px_str = _PxString(my_str)

    obj_a = _PxSingle("A")
    obj_a.set(my_px_str)
    act_a = obj_a.get_value()

    assert act_a == my_px_str

    my_key = _KeytypeLang("no")
    obj_b = _PxValueByKey("B")
    obj_b.set(my_px_str, my_key)
    act_b = obj_b.get_value(my_key)
    assert act_b == my_px_str


def test_reset_language_none_to_raises():
    my_key_no = _KeytypeLang("no")
    my_key_none = _KeytypeLang(None)
    a_value = "string"

    obj_b = _PxValueByKey("MYKEYWORD")

    obj_b.set(a_value, my_key_none)
    obj_b.set(a_value, my_key_no)

    with pytest.raises(ValueError, match="Duplicate key for MYKEYWORD "):
        obj_b.reset_language_none_to("no")
