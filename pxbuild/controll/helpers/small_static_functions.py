from typing import Dict, List

# Class for small static functions. 
class Commons:
  @staticmethod
  def get_variable_list(stub:List[str], heading:List[str] ) -> List[str]:
        return stub + heading