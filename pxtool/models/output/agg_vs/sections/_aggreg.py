from pxtool.models.output.agg_vs.sections._VS_super import _VS_super
class _Aggreg(_VS_super): 
    key_value_rows:list = []
    
    def __init__(self) -> None:
        self.section = "[Aggreg]"
        self.key_value_rows.clear()
        
    def set(self,vskey:str,vsvalue:str):
        
        self._vskey = vskey
        self._vsvalue = vsvalue
        my_dict= {"key":self._vskey,"val":self._vsvalue}
        self.key_value_rows.append((my_dict))

    def __str__(self):
        out_str = f"{self.section}\n"
        
        for my_dict  in self.key_value_rows:
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"
        return out_str
        