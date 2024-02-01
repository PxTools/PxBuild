import pytest
from pxbuild.models.output.pxfile.util._px_valuetype import _PxStringList


def test_PxStringList_wrong_type_raises():
    with pytest.raises(ValueError, match="list_of_strings must be list not <class 'str'>"):
        my_px_str = _PxStringList("a string")


def test_PxStringList_empty_raises():
    with pytest.raises(ValueError, match="list_of_strings must have a least one value"):
        my_px_str = _PxStringList([])
