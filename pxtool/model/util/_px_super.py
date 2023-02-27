class _PXSingle:
    """For data just the keyword, no need for a dict."""
    _keyword: str

    def __init__(self, keyword) -> None:
        self._keyword = keyword

    def set(self, px_value) -> None:
        if self.has_value():
           raise ValueError(f"Duplicate use. First value {self._px_value}, second value {px_value}.")
        self._px_value = px_value

    def get(self) -> None:
        return self._px_value.getValue()

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

    def get(self, my_key) -> None:
        return self._valueByKey[my_key].getValue()


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

