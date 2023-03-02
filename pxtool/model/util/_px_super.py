from pxtool.model.util._px_valuetype import _PxBool, _PxData, _PxHierarchy, _PxInt, _PxString, _PxStringList, _PxTlist

class _PxSingle:
    """For data just the keyword, no need for a dict."""
    _keyword: str

    def __init__(self, keyword) -> None:
        self._keyword = keyword

    def set(self, px_value:_PxInt | _PxString | _PxStringList | _PxBool | _PxData) -> None:
        if self.has_value():
           raise ValueError(f"Duplicate use. First value {self._px_value}, second value {px_value}.")
        self._px_value = px_value

    def get_value(self) -> _PxInt | _PxString | _PxStringList | _PxBool | _PxData:
        return self._px_value.get_value()

    def __str__(self):
        if self.has_value():
            return f"{self._keyword}={self._px_value};"
        else:
            return ""

    def has_value(self) -> bool:
        return hasattr(self,"_px_value")

class _PxValueByKey:
    """_PXValueByKey for data in a dict"""
    _keyword: str

    def __init__(self, keyword) -> None:
        self._keyword = keyword
        self._value_by_key = {}
        

    def set(self, px_value, my_key) -> None:
        if my_key in self._value_by_key.keys():
            raise ValueError(f"Duplicate key {my_key}, first value {self._value_by_key[my_key]}, second value {px_value}.")
        self._value_by_key[my_key] = px_value

    def get_value(self, my_key) -> _PxInt | _PxString | _PxStringList | _PxBool |_PxHierarchy | _PxTlist:
        return self._value_by_key.get(my_key)


    def __str__(self):
        myOut = []
        
        if self.has_value():
          for keypart in self._value_by_key.keys() :
              myOut.append(f"{self._keyword}{keypart} = {self._value_by_key[keypart]};") 
          return "\n".join(myOut)
        else:
            return ""  

    def __len__(self):
        return len(self._value_by_key)
    
    def has_value(self) -> bool:
        return len(self._value_by_key) > 0

