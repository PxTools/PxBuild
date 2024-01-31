import pytest
from pxbuild.models.output.pxfile.util._px_super import _PxSingle, _PxValueByKey, _SuperKeyword
from pxbuild.models.output.pxfile.util._px_valuetype import _PxString
from pxbuild.models.output.pxfile.util._px_keytypes import _KeytypeLang


def test_super():
    my_str = "a string"

    my_px_str = _PxString(my_str)

    objA = _PxSingle("A")
    objA.set(my_px_str)
    actA = objA.get_value()

    assert actA == my_px_str

    my_key = _KeytypeLang("no")
    objB = _PxValueByKey("B")
    objB.set(my_px_str, my_key)
    actB = objB.get_value(my_key)
    assert actB == my_px_str

    lengthB = len(objB)


def test_reset_language_none_to_raises():
    my_key_no = _KeytypeLang("no")
    my_key_none = _KeytypeLang(None)
    a_value = "string"

    objB = _PxValueByKey("MYKEYWORD")

    objB.set(a_value, my_key_none)
    objB.set(a_value, my_key_no)

    with pytest.raises(ValueError, match="Duplicate key for MYKEYWORD "):
        objB.reset_language_none_to("no")
