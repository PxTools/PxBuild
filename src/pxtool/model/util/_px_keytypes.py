"""
These classes have 2 purposes: 
  act as key in dictionary 
  write the keypart nicely

They used to be just namedTuples, but we wanted to use pydantic for validation  
"""
from model.util._line_validator import LineValidator

class _keytype_lang():
    lang:str = None

    def __init__(self, lang:str) -> None:
        if lang:
           LineValidator.is_string("language in key", lang)
           LineValidator.regexp_string("^[a-z]{2}$", "language in key", lang)
        self.lang=lang
        
    def __str__(self):
        return  f"[\"{self.lang}\"]" if self.lang else "" 

    def __eq__(self, other):
        if isinstance(other, _keytype_lang):
            return self.lang == other.lang
        return False

    def __hash__(self):
        return hash(self.lang)  

class _keytype_variable_lang(_keytype_lang):
    variable:str

    def __init__(self, variable:str, lang:str) -> None:
        super().__init__(lang)
        self.variable = variable

    def __str__(self):
         return  f"{super().__str__()}(\"{self.variable}\")"
    
    def __eq__(self, other):
        if isinstance(other, _keytype_variable_lang):
            return self.variable == other.variable and self.lang == other.lang
        return False

    def __hash__(self):
        return hash((self.variable, self.lang))  
    

class _keytype_content_lang(_keytype_lang):
    content:str

    def __init__(self, content:str, lang:str) -> None:
        super().__init__(lang)
        self.content = content

    def __str__(self):
          return  f"{super().__str__()}(\"{self.content}\")"
    
    def __eq__(self, other):
        if isinstance(other, _keytype_content_lang):
            return self.content == other.content and self.lang == other.lang
        return False

    def __hash__(self):
        return hash((self.content, self.lang))  

    def to_str_message(self) -> str:
         return  f"for language '{self.lang}' and variable '{self.variable}'"

class _keytype_variable_value_lang(_keytype_lang):
    variable:str
    value:str

    def __init__(self, variable:str, value:str, lang:str) -> None:
        super().__init__(lang)
        self.variable = variable
        self.value = value
    
    def __str__(self):
        return  f"{super().__str__()}(\"{self.variable}\",\"{self.value}\")"
    
    def __eq__(self, other):
        if isinstance(other, _keytype_variable_value_lang):
            return self.variable == other.variable and self.value == other.value and self.lang == other.lang
        return False

    def __hash__(self):
        return hash((self.variable, self.value, self.lang))  
    

    
class _keytype_variable_value():
    variable:str
    value:str

    def __init__(self, variable:str, value:str) -> None:
        self.variable = variable
        self.value = value
    
    def __str__(self):
        return  f"(\"{self.variable}\",\"{self.value}\")"   

    def __eq__(self, other):
        if isinstance(other, _keytype_variable_value):
            return self.variable == other.variable and self.value == other.value
        return False

    def __hash__(self):
        return hash((self.variable, self.value))   


class _keytype_variable_lang_multi(_keytype_variable_lang):
    counter:int

    def __init__(self, variable:str, lang:str, counter:int) -> None:
        super().__init__(variable,lang)
        self.counter = counter

    def __eq__(self, other):
        if isinstance(other, _keytype_variable_lang_multi):
            return self.variable == other.variable and self.lang == other.lang and self.counter == other.counter
        return False

    def __hash__(self):
        return hash((self.variable, self.lang, self.counter))

class _keytype_variable_value_lang_multi(_keytype_variable_value_lang):
    counter:int 

    def __init__(self, variable:str, value:str, lang:str, counter:int) -> None:
        super().__init__(variable, value, lang)
        self.counter = counter

    def __eq__(self, other):
        if isinstance(other, _keytype_variable_value_lang):
            return self.variable == other.variable and self.value == other.value and self.lang == other.lang and self.counter == other.counter
        return False

    def __hash__(self):
        return hash((self.variable, self.value, self.lang, self.counter))  
    



#_keytype_values_lang_multi = namedtuple("ValuesLangMulti", ['values', 'lang', 'counter'] )
class _keytype_values_lang_multi(_keytype_lang):
    values:list[str] 
    counter:int
    _joined:str

    def __init__(self, values:list[str], lang:str, counter:int) -> None:
        super().__init__(lang)
        self.values = values
        self.counter = counter
        self._joined = "\",\"".join(self.values)


    def __str__(self):
        return  f"{super().__str__()}(\"{self._joined}\")"
    
    def __eq__(self, other):
        if isinstance(other, _keytype_values_lang_multi):
            return self._joined == other._joined and self.lang == other.lang and self.counter == other.counter
        return False

    def __hash__(self):
        return hash((self._joined, self.lang, self.counter))  


class _keytype_values_multi(): 
    values:list[str] 
    counter:int
    _joined:str

    def __init__(self, values:list[str], counter:int) -> None:
        super().__init__()
        self.values = values
        self.counter = counter
        self._joined = "\",\"".join(self.values)

    def __str__(self):
        return  f"(\"{self._joined}\")"
    
    def __eq__(self, other):
        if isinstance(other, _keytype_values_multi):
            return self._joined == other._joined and self.lang == other.lang and self.counter == other.counter
        return False

    def __hash__(self):
        return hash((self._joined, self.lang, self.counter))  
