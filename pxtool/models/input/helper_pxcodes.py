from .pydantic_pxcodes import PxCodes
from typing import Dict, List, Optional

class HelperPxCodes:
    def __init__(self,inPxCodes:PxCodes) -> None:
        self._pxcodes= inPxCodes
        self.elimination_possible = inPxCodes.elimination_possible


    def getCodes(self, language) -> List[str]:
        out_codes=[]
          
        #TODO:  sortert liste
        for code in self._pxcodes.valueitems:
             out_codes.append(code.code)
        return out_codes
      
    def getLabels(self, language) -> List[str]:
        out_values =[]
        #TODO:  sortert liste
        for code in self._pxcodes.valueitems:
            out_values.append(code.label[language])

        return out_values
    


    def getEliminationLabel(self, language) -> str:
        myOut:str = ""
        if self._pxcodes.elimination_possible:
            if self._pxcodes.elimination_code:
                #need to find label ...
                for item in self._pxcodes.valueitems:
                   if item.code == self._pxcodes.elimination_code:
                      myOut = item.label[language]
                      break  
        return myOut


