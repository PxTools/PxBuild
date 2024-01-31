import pytest
from pxbuild.models.output.pxfile.keywords._attributes import _Attributes


def test_set_valid():
    obj = _Attributes()
    obj.set(["A", "F"], ["01", "A01", "2005"])
    assert obj.get_value(["01", "A01", "2005"]) == ["A", "F"]


def test_Attributes_hack_multi_duplicate_set_raises():
    obj = _Attributes()
    obj.set(["a string"], ["another string"])
    obj.occurence_counter = 0
    with pytest.raises(Exception) as err_mess:
        obj.set(["a string"], ["another string"])
    assert str(err_mess.value).startswith("ATTRIBUTES:")
