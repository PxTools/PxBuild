import re


class LineValidator:
    """Some validations, they raise ValueError or return None.
    They have the keyword and input-value(s) as the last parameters
    """

    @staticmethod
    def is_not_None(keyword: str, input_value) -> None:
        if input_value is None:
            raise ValueError(f"{keyword}: value is empty")

    @staticmethod
    def is_int(keyword: str, input_value: int) -> None:
        if not isinstance(input_value, int):
            raise ValueError(f"{keyword}:value must be an integer, got type {type(input_value).__name__}.")

    @staticmethod
    def is_string(keyword: str, input_value: str) -> None:
        if not isinstance(input_value, str):
            raise ValueError(f"{keyword}:value must be a string, got type {type(input_value).__name__}.")

    @staticmethod
    def is_bool(keyword: str, input_value: bool) -> None:
        if not isinstance(input_value, bool):
            raise ValueError(f"{keyword}:value must be an bool, got type {type(input_value).__name__}.")

    @staticmethod
    def is_list_of_strings(keyword: str, input_value: list[str]) -> None:
        # is list
        if not isinstance(input_value, list):
            raise ValueError(f"{keyword}:value must be a list of strings, got type {type(input_value).__name__}.")
        # has items
        if len(input_value) < 1:
            raise ValueError(f"{keyword}:the list is empty.")
        # all items are strings
        for item in input_value:
            if not isinstance(item, str):
                raise ValueError(f"{keyword}:the item {item} is not a string but a {type(item).__name__}")

    # -----------------------------  values

    @staticmethod
    def in_range(lower_bound: int, upper_bound: int, keyword: str, input_value: int) -> None:
        """input_value:int"""
        if input_value < lower_bound:
            raise ValueError(f"{keyword}:value {input_value} must be greater than or equal to {lower_bound}.")
        if input_value > upper_bound:
            raise ValueError(f"{keyword}:value {input_value} must be less than or equal to {upper_bound}.")

    @staticmethod
    def regexp_string(reg_exp: str, keyword: str, input_value: str) -> None:
        match = re.search(reg_exp, input_value)
        if not match:
            raise ValueError(f"{keyword}:the value {input_value} does not match regexp {reg_exp}")

    @staticmethod
    def regexp_item_string(reg_exp: str, keyword: str, input_value: list[str]) -> None:
        itemindex: int = 0
        for item in input_value:
            itemindex += 1
            match = re.search(reg_exp, item)
            if not match:
                raise ValueError(
                    f"{keyword}:value {input_value} (item no: {itemindex} ) does not match regexp {reg_exp}"
                )

    @staticmethod
    def unique(keyword: str, input_value: list[str]) -> None:
        for item in input_value:
            if input_value.count(item) > 1:
                raise ValueError(f"{keyword}:item {item} is a duplicate")
