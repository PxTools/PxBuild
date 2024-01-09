from typing import List, Dict
from pxtool.controll.helpers.for_get_data import ForGetData


class DataFormatter:
    def __init__(self, heading: List[str], variables: Dict[str, ForGetData]) -> None:
        self._heading = heading
        self._variables = variables

    def calculate_line_break(self) -> int:
        linebreak_counter = 1
        for key, value in self._variables.items():
            if key in self._heading:
                linebreak_counter = linebreak_counter * value._length_of_codelist

        return linebreak_counter
