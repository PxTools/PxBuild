import pytest
from pxbuild.models.output.pxfile.util._line_validator import LineValidator


def test_is_not_none_raises():
    with pytest.raises(Exception, match="MY_KEYWORD: value is empty"):
        LineValidator.is_not_None("MY_KEYWORD", None)


def test_is_int_raises():
    with pytest.raises(Exception, match="MY_KEYWORD:value must be an integer, got type str."):
        LineValidator.is_int("MY_KEYWORD", "a string")


def test_is_string_raises():
    with pytest.raises(Exception, match="MY_KEYWORD:value must be a string, got type int."):
        LineValidator.is_string("MY_KEYWORD", 1)


def test_is_bool_raises():
    with pytest.raises(Exception, match="MY_KEYWORD:value must be an bool, got type int."):
        LineValidator.is_bool("MY_KEYWORD", 1)


def test_is_list_of_strings_raises_not_list():
    with pytest.raises(Exception, match="MY_KEYWORD:value must be a list of strings, got type str."):
        LineValidator.is_list_of_strings("MY_KEYWORD", "1")


def test_is_list_of_strings_raises_empty():
    with pytest.raises(Exception, match="MY_KEYWORD:the list is empty."):
        LineValidator.is_list_of_strings("MY_KEYWORD", [])


def test_is_list_of_strings_raises_not_all_string():
    with pytest.raises(Exception, match="MY_KEYWORD:the item 3 is not a string but a int"):
        LineValidator.is_list_of_strings("MY_KEYWORD", ["1", "2", 3, "4"])


def test_in_range_raises_lower_boundary():
    with pytest.raises(Exception, match="MY_KEYWORD:value 1 must be greater than or equal to 2."):
        LineValidator.in_range(2, 3, "MY_KEYWORD", 1)


def test_in_range_raises_upper_boundary():
    with pytest.raises(Exception, match="MY_KEYWORD:value 4 must be less than or equal to 3"):
        LineValidator.in_range(2, 3, "MY_KEYWORD", 4)


def test_unique_raises():
    with pytest.raises(Exception, match="MY_KEYWORD:item 14 is a duplicate"):
        LineValidator.unique("MY_KEYWORD", [2, 3, 14, 14])
    with pytest.raises(Exception, match="MY_KEYWORD:item 14 is a duplicate"):
        LineValidator.unique("MY_KEYWORD", [2, 3, "14", "14"])
