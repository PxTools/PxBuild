import pytest
from pxtool.model.keywords._contents import _Contents
    
def test_Contents_set_valid():
    obj = _Contents("CONTENTS")
    obj.set("a string","no")
    assert obj.get_value("no") == "a string"
    
def test_Contents_duplicate_set_raises():
    obj = _Contents("CONTENTS")
    obj.set("a string","no")
    with pytest.raises(Exception):
        obj.set("a string","no")
