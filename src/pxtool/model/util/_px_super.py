from collections import namedtuple

class _PXSingle:
    """For data just the keyword, no need for a dict."""
    _keyword: str

    def __init__(self, keyword) -> None:
        self._keyword = keyword

    def set(self, px_value) -> None:
        if self.has_value():
           raise ValueError(f"Duplicate use. First value {self._px_value}, second value {px_value}.")
        self._px_value = px_value

    def __str__(self):
        if self.has_value():
            return f"{self._keyword}={self._px_value};"
        else:
            return ""

    def has_value(self) -> bool:
        return hasattr(self,"_px_value")

class _PXValueByKey:
    """_PXValueByKey for data in a dict"""
    _keyword: str

    def __init__(self, keyword) -> None:
        self._keyword = keyword
        self._valueByKey = {}
        

    def set(self, px_value, my_key) -> None:
        if my_key in self._valueByKey.keys():
            raise ValueError(f"Duplicate key {my_key}, first value {self._valueByKey[my_key]}, second value {px_value}.")
        self._valueByKey[my_key] = px_value

    def __str__(self):
        myOut = []
        
        if self.has_value():
          for keypart in self._valueByKey.keys() :
              myOut.append(f"{self._keyword}{keypart} = {self._valueByKey[keypart]};") 
          return "\n".join(myOut)
        else:
            return ""  

    def __len__(self):
        return len(self._valueByKey)
    
    def has_value(self) -> bool:
        return len(self._valueByKey) > 0


#---------------   ValueType Classes:
class _PxTlist:
    """ TLIST(A1, ”1994”-”1996”);  eller TLIST(A1), ”1994”, ”1995”,"1996”;  """
    def __init__(self, timescale:str, time_periods:list[str]) -> None:
        self.timescale= timescale
        self.time_periods = time_periods

    def __str__(self):
        listAsString = f"\",\"".join(self.time_periods)
        return f"TLIST({self.timescale}),\"{listAsString}\""        

class _PxHierarchy:
    """ HIERARCHIES(“Country”)="parent","parent":"child",..."""
    def __init__(self, root_node:str, mother_child:dict[str,str]) -> None:
        self.root_node = root_node
        self.mother_child = mother_child

    def __str__(self):
        return self.root_node + ', '.join(['{}:{}'.format(k, v) for k, v in self.mother_child.items()])


class _PxStringList:
    """ Holdes a list of stings and prints them quotes separated by comma  """
    def __init__(self, list_of_strings:list[str]) -> None:
        self.list_of_strings = list_of_strings
        if not type(list_of_strings) == list:
            raise ValueError(f"list_of_strings must be list not {type(list_of_strings)}")
        if len(list_of_strings) < 1:
            raise ValueError(f"list_of_strings must have a least one value")

    def __str__(self):
            listAsString = f"\",\"".join(self.list_of_strings)
            return f"\"{listAsString}\""            

    def __len__(self):
        return len(self.list_of_strings)

class _PxString:
    """ Holdes a sting and prints it in quotes """
    def __init__(self, _string:str) -> None:
        self._string = _string

    def __str__(self):
            return f"\"{self._string}\""

class _PxBool:
    """ Holdes a bool and prints it as YES or NO """
    def __init__(self, _bool:bool) -> None:
        self._bool = _bool

    def __str__(self):
            return "YES" if self._bool else"NO"

class _PxData:
    def __init__(self, the_data:list) -> None:
        self.data = the_data


    def __str__(self):
            return " ".join(self.data)

        







                        

            