from typing import Dict, List

# Class for small static functions. 
class Commons:
  @staticmethod
  def get_variable_list(stub:List[str], heading:List[str] ) -> List[str]:
        return stub + heading
  

  @staticmethod
  def make_domain_id(code_list_id: str, language: str) -> str:
    domain_id = code_list_id + "_" + language
    return domain_id