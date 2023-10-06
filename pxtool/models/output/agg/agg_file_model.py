from pxtool.models.output.agg_vs.sections._description import _Description
from pxtool.models.output.agg_vs.sections._aggreg import _Aggreg
from pxtool.models.output.agg_vs.sections._domain import _Domain
from pxtool.models.output.agg_vs.sections._valuecode import _Valuecode
from pxtool.models.output.agg_vs.sections._valuetext import _Valuetext

class _AggFileModel():
    aggreg_list =[]
    aggtext_list=[]
    code_list=[]
    #key_value_rows:list = []
    
    # def __init__(self,name,valueset) -> None:
    #     self.name= name
    #     self.valueset= valueset
    def __init__(self) -> None:
        self.aggreg_list.clear()
        self.aggtext_list.clear()
        self.code_list.clear()
        print("i init ailemodel")

        
    def set(self,section:str,vskey:str,vsvalue:str): 
        _section= section   
        _vskey = vskey
        _vsvalue = vsvalue
        my_value_dict= {"key":_vskey,"val":_vsvalue}
        if _section=="Aggreg":
            self.aggreg_list.append(my_value_dict)
        elif _section=="Aggtext":
            self.aggtext_list.append(my_value_dict)
        else:
            my_code_dict={"section":_section,"key":_vskey,"val":_vsvalue}
            self.code_list.append(my_code_dict)
            
            
        # my_section_dict = {"section":my_value_dict} 
        # self.key_value_rows.append((my_section_dict))
        
    def __str__(self):
        
        
        out_str = "[Aggreg] \n"
        for my_dict  in self.aggreg_list:
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"

        out_str = out_str + "[Aggtext] \n"
        for my_dict  in self.aggtext_list:
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"

        previous_section_key= ""
        for my_dict  in self.code_list:
            section_key = my_dict.get("section")
            if section_key != previous_section_key:
                out_str = out_str + "[" + section_key + "] \n"    
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"
            previous_section_key= section_key

        return out_str