﻿import pytest
from pxbuild.models.output.pxfile.util._px_valuetype import _PxStringList


def test_pxstringlist_wrong_type_raises():
    with pytest.raises(ValueError, match="list_of_strings must be list not <class 'str'>"):
        _PxStringList("a string")


def test_pxstringlist_empty_raises():
    with pytest.raises(ValueError, match="list_of_strings must have a least one value"):
        _PxStringList([])
