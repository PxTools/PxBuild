# ---------------   ValueType Classes:
import datetime
from typing import Optional

class _PxTlist: 
    """TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”;"""

    def __init__(self, timescale: str, time_periods: list[str]) -> None:
        self.timescale = timescale
        self.time_periods = time_periods
        
    def __str__(self):
        return self.parse_timeval(self.time_periods)

    def get_value(self):
        return (self.timescale, self.time_periods)
    
    def parse_timeval(self, periods: list[str]) -> str:

        def parse_period(date_str: str) -> tuple[int, str, int]:
            year = int(date_str[:4])
            period_type = date_str[4] if len(date_str) > 4 else 'A'
            period_value = int(date_str[5:]) if len(date_str) > 4 else 1
            return year, period_type, period_value

        def weeks_in_year(year: int) -> int:
            last_day_of_year = datetime.date(year, 12, 31)
            week_number = last_day_of_year.isocalendar()[1]
            return week_number

        def get_period_length(year: int, period_type: str) -> int:
            period_lengths = {
                'M': 12,
                'Q': 4,
                'H': 2,
                'W': weeks_in_year(year),
                'A': 1
            }
            return period_lengths[period_type]

        def period_difference(year1: int, period1: int, year2: int, period2: int, period_type: str) -> int:
            return (year2 - year1) * get_period_length(year1, period_type) + (period2 - period1)

        def check_consistent_gap(dates: list[str]) -> tuple[bool, Optional[int]]:
            parsed_dates = [parse_period(date) for date in dates]
            period_type = parsed_dates[0][1]
            
            # Calculate the initial gap from the first two periods
            year1, _, period1 = parsed_dates[0]
            year2, _, period2 = parsed_dates[1]
            initial_gap = period_difference(year1, period1, year2, period2, period_type)
            
            # Check if all subsequent gaps are equal to the initial gap
            for i in range(2, len(parsed_dates)):
                year1, _, period1 = parsed_dates[i-1]
                year2, _, period2 = parsed_dates[i]
                actual_gap = period_difference(year1, period1, year2, period2, period_type)
                if actual_gap != initial_gap:
                    return False, None
            return True, initial_gap

        def fill_gaps(periods: list[str]) -> list[str]:
            start_year, period_type, start_period = parse_period(periods[0])
            end_year, _, end_period = parse_period(periods[-1])
            filled_periods = []
            for year in range(start_year, end_year + 1):
                max_period = get_period_length(year, period_type)
                for period in range(1, max_period + 1):
                    period_str = f"{year}{period_type}{period:02d}" if period_type != 'A' else f"{year}"
                    filled_periods.append(period_str)
            return filled_periods[int(start_period)-1:int(len(filled_periods)-(max_period-end_period))]

        # Convert integer years to string format
        periods = [str(period) for period in periods]

        if len(periods) == 1:
            period_type = parse_period(periods[0])[1]
            return f'TLIST({period_type}1,"{periods[0]}")'

        consistent_gap, gap_size = check_consistent_gap(periods)
        period_type = parse_period(periods[0])[1]

        if consistent_gap:
            if gap_size == 1:
                return f'TLIST({period_type}1,"{periods[0]}-{periods[-1]}")'
            filled_periods = fill_gaps(periods)
            periods_int = [str(''.join(filter(str.isdigit, t))) for t in filled_periods]
            return f'TLIST({period_type}1,"{",".join(periods_int)}")'
        periods_int = [str(''.join(filter(str.isdigit, t))) for t in periods]
        return f'TLIST({period_type}1,"{",".join(periods_int)}")'

class _PxHierarchy:
    """HIERARCHIES(“Country”)="parent","parent":"child",..."""

    def __init__(self, root_node: str, mother_child: dict[str, str]) -> None:
        self.root_node = root_node
        self.mother_child = mother_child

    def __str__(self):
        return self.root_node + ", ".join(["{}:{}".format(k, v) for k, v in self.mother_child.items()])

    def get_value(self):
        return (self.root_node, self.mother_child)


class _PxStringList:
    """Holdes a list of stings and prints them quotes separated by comma"""

    def __init__(self, list_of_strings: list[str]) -> None:
        self.list_of_strings = list_of_strings
        if type(list_of_strings) is not list:
            raise ValueError(f"list_of_strings must be list not {type(list_of_strings)}")
        if len(list_of_strings) < 1:
            raise ValueError(f"list_of_strings must have a least one value")

    def __str__(self):
        list_as_string = f'","'.join(self.list_of_strings)
        return f'"{list_as_string}"'

    def __len__(self):
        return len(self.list_of_strings)

    def get_value(self):
        return self.list_of_strings


class _PxString:
    """Holdes a sting and prints it in quotes"""

    def __init__(self, _string: str) -> None:
        self._string = _string

    def __str__(self):
        return f'"{self._string}"'

    def get_value(self):
        return self._string


class _PxBString:
    """Holdes a sting or bool and prints it in quotes only if string"""

    def __init__(self, _string: str) -> None:
        self._string = _string

    def __str__(self):
        if self._string == "YES" or self._string == "NO":
            return self._string

        return f'"{self._string}"'

    def get_value(self):
        return self._string


class _PxBool:
    """Holdes a bool and prints it as YES or NO"""

    def __init__(self, _bool: bool) -> None:
        self._bool = _bool

    def __str__(self):
        return "YES" if self._bool else "NO"

    def get_value(self):
        return self._bool


class _PxData:
    def __init__(self, the_data: list, columns_per_line: int) -> None:
        self._data = the_data
        self._columns_per_line = columns_per_line

    def __str__(self):
        data_string = ""
        for i, data_cell in enumerate(self._data):
            if i > 0:
                if i % self._columns_per_line == 0:
                    data_string += "\n"
                else:
                    data_string += " "
            data_string += data_cell

        return data_string

    def get_value(self):
        return self._data


class _PxInt:
    """Holdes a integer and prints it in quotes"""

    def __init__(self, _int: int) -> None:
        self._int = _int

    def __str__(self):
        return f"{self._int}"

    def get_value(self) -> int:
        return self._int
