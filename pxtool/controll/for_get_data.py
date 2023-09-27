from typing import List

class ForGetData:
    """ Helper class for data extraction """

    def __init__(self, colname_in_dataframe:str,codelist:List[str] ) -> None:
       self._colname_in_dataframe:str = colname_in_dataframe
       
       self._position_of_value = {string: index for index, string in enumerate(codelist)}
       """ Dict holding position in codelist as a function of the code """

       self._length_of_codelist = len(codelist)

       self.factor:int = -1
       """This depends on the desired output order of the variables. Is the (math) product of _length_of_codelist of the previous variables """

    def getIndexContrib(self,row) -> int:
        myCode = row[self._colname_in_dataframe]
        if not myCode in self._position_of_value:
          print("Cant find ",myCode, "in", self._position_of_value.keys())

        myPos = self._position_of_value[myCode]

        #print("faktor:",self.factor, "myPos", myPos )

        return self.factor*myPos
    

    def GetDebugString(self) -> List:
       return ["colname", self._colname_in_dataframe, "N:", self._length_of_codelist, "self.factor", self.factor]
    
    
