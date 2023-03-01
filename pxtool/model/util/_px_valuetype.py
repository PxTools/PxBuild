#---------------   ValueType Classes:
class _PxTlist:
    """ TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”;  """
    def __init__(self, timescale:str, time_periods:list[str]) -> None:
        self.timescale= timescale
        self.time_periods = time_periods

    def __str__(self):
        list_as_string = f"\",\"".join(self.time_periods)
        return f"TLIST({self.timescale}),\"{list_as_string}\"" 

    def getValue(self):
        return (self.timescale,self.time_periods)       

class _PxHierarchy:
    """ HIERARCHIES(“Country”)="parent","parent":"child",..."""
    def __init__(self, root_node:str, mother_child:dict[str,str]) -> None:
        self.root_node = root_node
        self.mother_child = mother_child

    def __str__(self):
        return self.root_node + ', '.join(['{}:{}'.format(k, v) for k, v in self.mother_child.items()])

    def getValue(self):
        return (self.root_node,self. mother_child)    


class _PxStringList:
    """ Holdes a list of stings and prints them quotes separated by comma  """
    def __init__(self, list_of_strings:list[str]) -> None:
        self.list_of_strings = list_of_strings
        if not type(list_of_strings) == list:
            raise ValueError(f"list_of_strings must be list not {type(list_of_strings)}")
        if len(list_of_strings) < 1:
            raise ValueError(f"list_of_strings must have a least one value")

    def __str__(self):
            list_as_string = f"\",\"".join(self.list_of_strings)
            return f"\"{list_as_string}\""            

    def __len__(self):
        return len(self.list_of_strings)
    
    def getValue(self):
        return self.list_of_strings    

class _PxString:
    """ Holdes a sting and prints it in quotes """
    def __init__(self, _string:str) -> None:
        self._string = _string

    def __str__(self):
            return f"\"{self._string}\""
    
    def getValue(self):
        return self._string
    
class _PxBool:
    """ Holdes a bool and prints it as YES or NO """
    def __init__(self, _bool:bool) -> None:
        self._bool = _bool

    def __str__(self):
            return "YES" if self._bool else"NO"
    
    def getValue(self):
        return self._bool

class _PxData:
    def __init__(self, the_data:list) -> None:
        self._data = the_data


    def __str__(self):
            return " ".join(self._data)
    
    def getValue(self):
        return self._data
    
class _PxInt:
    """ Holdes a integer and prints it in quotes """
    def __init__(self, _int:int) -> None:
        self._int = _int

    def __str__(self):
            return f"\"{self._int}\""
    
    def getValue(self):
        return self._int        