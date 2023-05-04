import pytest
from pxtool.model.util._px_super import _PxSingle, _PxValueByKey
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._px_keytypes import _KeytypeLang

def test_super():
    my_str = "a string"
    
    my_px_str=_PxString(my_str)

    objA = _PxSingle("A")
    objA.set(my_px_str)
    actA = objA.get_value()
    
    assert actA == my_px_str

    my_key = _KeytypeLang("no")
    objB = _PxValueByKey("B")
    objB.set(my_px_str,my_key)
    actB = objB.get_value(my_key)
    assert  actB == my_px_str






