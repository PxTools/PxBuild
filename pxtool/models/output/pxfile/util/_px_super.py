from pxtool.models.output.pxfile.util._px_valuetype import _PxBool, _PxData, _PxHierarchy, _PxInt, _PxString, _PxStringList, _PxTlist
from abc import ABC, abstractmethod


class _SuperKeyword(ABC):
    _keyword: str

    def __init__(self, keyword) -> None:
        self._keyword = keyword

    @abstractmethod
    def is_present(self) -> bool: # pragma: no cover
        pass

class _PxSingle(_SuperKeyword):
    """For data just the keyword, no need for a dict."""

    def __init__(self, keyword) -> None:
        super().__init__(keyword)

    def set(self, px_value:_PxInt | _PxString | _PxStringList | _PxBool | _PxData) -> None:
        if self.is_present():
           raise ValueError(f"Duplicate use. First value {self._px_value}, second value {px_value}.")
        self._px_value = px_value

    def get_value(self) -> _PxInt | _PxString | _PxStringList | _PxBool | _PxData:
        return self._px_value

    def __str__(self):
        if self.has_value():
            return f"{self._keyword}={self._px_value};"
        else:
            return ""

    def has_value(self) -> bool:
        return hasattr(self,"_px_value")
    
    def is_present(self) -> bool:
        return hasattr(self,"_px_value")

class _PxValueByKey(_SuperKeyword):
    """_PXValueByKey for data in a dict"""

    def __init__(self, keyword) -> None:
        super().__init__(keyword)
        self._value_by_key = {}

    def set(self, px_value, my_key) -> None:
        if my_key in self._value_by_key.keys():
            raise ValueError(f"Duplicate key {my_key}, first value {self._value_by_key[my_key]}, second value {px_value}.")
        self._value_by_key[my_key] = px_value

    def get_value(self, my_key) -> _PxInt | _PxString | _PxStringList | _PxBool |_PxHierarchy | _PxTlist:
        return self._value_by_key.get(my_key)
    
    def has_value(self, my_key) -> _PxInt | _PxString | _PxStringList | _PxBool |_PxHierarchy | _PxTlist:
        return my_key in self._value_by_key


    def __str__(self):
        myOut = []
        
        if self.is_present():
          for keypart in self._value_by_key.keys() :
              myOut.append(f"{self._keyword}{keypart}={self._value_by_key[keypart]};") 
          return "\n".join(myOut)
        else:
            return ""  

    def __len__(self):
        return len(self._value_by_key)
    
    def is_present(self) -> bool:
        return len(self._value_by_key) > 0
    

    #for classes that may_have_language
    def reset_language_none_to(self,lang:str)->None:
        new_value_by_key = {}
        for old_key, value in self._value_by_key.items():
            new_key = old_key.reset_lang_none_to(lang)
            if new_key in new_value_by_key.keys():
                raise ValueError(f"Duplicate key for {self._keyword} {new_key}, when inserting default language")
            new_value_by_key[new_key] = value

        self._value_by_key = new_value_by_key




