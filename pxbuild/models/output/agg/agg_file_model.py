class AggFileModel:
    _aggreg_list = []
    _aggtext_list = []
    _code_list = []
    _code_dict = {}
    # key_value_rows:list = []

    # def __init__(self,name,valueset) -> None:
    #     self.name= name
    #     self.valueset= valueset
    def __init__(self) -> None:
        self._aggreg_list.clear()
        self._aggtext_list.clear()
        self._code_list.clear()
        self._code_dict = {}
        print("i init ailemodel")

    # def set(self,section:str,vskey:str,vsvalue:str):
    #     section= section
    #     vskey = vskey
    #     vsvalue = vsvalue
    #     my_value_dict= {"key":vskey,"val":vsvalue}
    #     if section=="Aggreg":
    #         self._aggreg_list.append(my_value_dict)
    #     elif section=="Aggtext":
    #         self._aggtext_list.append(my_value_dict)
    #     else:
    #         my_code_dict={"section":section,"key":vskey,"val":vsvalue}
    #         self._code_list.append(my_code_dict)
    def set(self, section: str, vskey: str, vsvalue: str):
        section = section
        vskey = vskey
        vsvalue = vsvalue
        my_value_dict = {"key": vskey, "val": vsvalue}
        if section == "Aggreg":
            self._aggreg_list.append(my_value_dict)
        elif section == "Aggtext":
            self._aggtext_list.append(my_value_dict)
        else:
            if section in self._code_dict.keys():
                self._code_dict.get(section).append({vskey: vsvalue})
            else:
                self._code_dict[section] = [{vskey: vsvalue}]

    def __str__(self):

        out_str = "[Aggreg] \n"
        for my_dict in self._aggreg_list:
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"

        out_str = out_str + "[Aggtext] \n"
        for my_dict in self._aggtext_list:
            out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"

        # previous_section_key= ""
        # for my_dict  in self._code_list:
        #     section_key = my_dict.get("section")
        #     if section_key != previous_section_key:
        #         out_str = out_str + "[" + section_key + "] \n"
        #     out_str = out_str + f"{my_dict['key']}={my_dict['val']} \n"
        #     previous_section_key= section_key

        for section in self._code_dict:
            out_str = out_str + "[" + section + "] \n"
            my_list = self._code_dict[section]
            for items in my_list:
                out_str = out_str + f"{list(items.keys())[0]}={items[list(items.keys())[0]]} \n"

        return out_str
