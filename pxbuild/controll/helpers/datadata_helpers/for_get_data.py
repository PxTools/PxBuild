from typing import List, Dict

class ForGetData:
    """ Helper class for data extraction """

    def __init__(self, colname_in_dataframe:str,codelist:List[str] ) -> None:
       self._colname_in_dataframe:str = colname_in_dataframe
       
       self._position_of_value = {string: index for index, string in enumerate(codelist)}
       """ Dict holding position in codelist as a function of the code """

       self._length_of_codelist = len(codelist)

       self.factor:int = -1
       """This depends on the desired output order of the variables. Is the (math) product of _length_of_codelist of the previous variables """

    def GetDebugString(self) -> List:
       return ["colname", self._colname_in_dataframe, "N:", self._length_of_codelist, "self.factor", self.factor]

    
