import csv
from collections import namedtuple
from re import sub

def DictAsSignature(inDict:dict) -> str:
    """Returns a dict as string in method signature (mystring:str, myint:int)"""
    return ', '.join(['{}:{}'.format(k, v) for k, v in inDict.items()])

def DictAsCall(inDict:dict) -> str:
    """Returns a dict as string in method call (mystring, myint)"""
    return ', '.join(inDict.keys())

def DictAsReturntype(inDict:dict) -> str:
    """Returns a dict as string in method call (str, int) or str if there is only one entry """
    my_out =  ', '.join(inDict.values())
    if ("," in my_out):
        my_out = f"({my_out})"
    return my_out


def to_python_case(text):
    return text.replace("-", "_").lower()

def to_camel_case(text) -> str:
    return sub(r"(_|-)+", " ", text).title().replace(" ", "")

def getKeyType(has_lang:bool,subkeys:dict,multi:bool) -> str:
       myOut = "" 
       if len(subkeys) > 0:
        myOut += "".join(key.capitalize() for key in subkeys.keys())
       if has_lang:
        myOut += "Lang"
       if multi:
         myOut += "Multi"
       if myOut :  
         myOut ="_Keytype"+myOut  
       return myOut


SpecRow = namedtuple("SpecRow", ['px_keyword', 'is_lang_dependent', 'is_Mandatory', 'completeness_type','med_ut','ut_default', 'px_SubKey', 'is_SubKey_Optional', 'is_duplicate_keypart_allowed_', 'px_valuetype', 'px_valuetype_params', 'linevalidate', 'px_comment','from_pdf'] )

#Tja, de er jo python typer alle sammen. Så det er vel typen til parameter i set funksjonen vs den typen som lagres value i super klassen
to_native_types={"_PxStringList":"list[str]","_PxString":"str","_PxBool":"bool","_PxInt":"int","_PxData":"list"}

#contains list of validation method-stubs for valueTypes. The keyWord and inputvalue is added in generation. 
valuetype_line_val = {"_PxStringList":["is_not_None(","is_list_of_strings("],"_PxString":["is_not_None(","is_string("],"_PxBool":["is_not_None(","is_bool("],"_PxInt":["is_not_None(","is_int("]}


class MyKeyword:
    def __init__(self,csvRow:SpecRow) -> None:
        self.keyword = csvRow.px_keyword
        self.has_lang = bool(csvRow.is_lang_dependent)
        self.is_mandatory = bool(csvRow.is_Mandatory)  #todo
        self.completeness_type = csvRow.completeness_type
        self.subkeys_raw = csvRow.px_SubKey
        self.is_SubKey_Optional = bool(csvRow.is_SubKey_Optional)
        self.is_duplicate_keypart_allowed = bool(csvRow.is_duplicate_keypart_allowed_)
        self.px_valuetype = csvRow.px_valuetype
        self.px_valuetype_params = csvRow.px_valuetype_params
        tmp_linevalidate = []
        if self.px_valuetype in valuetype_line_val.keys():
            tmp_linevalidate = valuetype_line_val[self.px_valuetype] 
        if csvRow.linevalidate:
           self.linevalidate = tmp_linevalidate + csvRow.linevalidate.split(" XX ")
        else:
           self.linevalidate = tmp_linevalidate

        self.px_comment = csvRow.px_comment
        

        #util

        self.module_name = "_"+to_python_case(self.keyword)

        #keyPart
        self.subkeys = {} if not self.subkeys_raw else dict((x.strip(), y.strip())
            for x, y in (element.split(':')
            for element in self.subkeys_raw.split(',')))
        self.keyParams = self.subkeys.copy()
        if self.has_lang:
            self.keyParams.update({'lang':"str = None"})

       
        #valuePart

        self.valueParams={}
        if self.px_valuetype in to_native_types:
            self.valueParams.update({ to_python_case(self.keyword) : to_native_types[self.px_valuetype] })
        elif self.px_valuetype_params:
            self.valueParams= dict((x.strip(), y.strip())
                for x, y in (element.split(':')
                for element in self.px_valuetype_params.split(', ')))
        else: 
            self.valueParams.update({"TODO":"str"})
          
        
        params_in_setDict = self.valueParams.copy()
        if self.keyParams:
            params_in_setDict.update(self.keyParams.items())

        self.params_in_set = DictAsSignature(params_in_setDict)

        #ClassNames

        self.classnames={}
        self.classnames["This"] = "_"+to_camel_case(self.keyword)
        self.classnames["Value"]= self.px_valuetype
        self.classnames["Key"] = getKeyType(self.has_lang,self.subkeys,self.is_duplicate_keypart_allowed)
        self.classnames["Super"]= "_PxValueByKey" if self.has_lang or self.subkeys_raw else "_PxSingle"

       #Constructors



    #Writers

    def imports_writer(self, fileHandle) -> None:
        fileHandle.write(f"from pxtool.model.util._px_super import {self.classnames['Super']}\n")
        if self.classnames["Value"] != "int" :
             fileHandle.write(f"from pxtool.model.util._px_valuetype import {self.classnames['Value']}\n")
        if self.classnames["Key"]:
            fileHandle.write(f"from pxtool.model.util._px_keytypes import { self.classnames['Key']}\n")
        fileHandle.write("from pxtool.model.util._line_validator import LineValidator\n\n")


    def class_and_init_writer(self, fileHandle) -> None:
        fileHandle.write(f"class {self.classnames['This']}({self.classnames['Super']}): \n\n")
        fileHandle.write(f"    pxvalue_type:str = \"{self.classnames['Value']}\"\n")
        if self.keyword == "LANGUAGES":
            pass
        fileHandle.write(f"    has_subkey:bool = {not self.subkeys_raw.strip() == ''}\n")
        fileHandle.write(f"    subkey_optional:bool = {self.is_SubKey_Optional }\n")
        fileHandle.write(f"    completeness_type:str = \"{self.completeness_type}\"\n")
        fileHandle.write(f"    may_have_language:bool = {self.has_lang}\n\n")

        fileHandle.write(f"    def __init__(self) -> None:\n")
        fileHandle.write(f"        super().__init__(\"{self.keyword}\")\n")
        if self.has_lang:
            fileHandle.write("        self._seen_languages={}\n")
        if self.is_duplicate_keypart_allowed:    
            fileHandle.write("        self.occurence_counter = 0\n")
        fileHandle.write(f"\n")

    def set_writer(self, fileHandle) -> None:
        fileHandle.write(f"    def set(self, {kw.params_in_set}) -> None:\n")
        fileHandle.write(f"        \"\"\" {kw.px_comment} \"\"\"\n")

        #LineValidator.              regexp_string("^(CODES|VALUES)$",   +   "mykeyword", "CODES")
        for item in kw.linevalidate:
            fileHandle.write(f"        LineValidator.{item} self._keyword, {DictAsCall(kw.valueParams)})\n")


        # valuetype_contructor
        fileHandle.write(f"        my_value = {self.classnames['Value']}({DictAsCall(self.valueParams)})\n")

        # keytype_contructor (except for "pure" keywords )
        if self.classnames["Key"]:
            if kw.is_duplicate_keypart_allowed:
                fileHandle.write(f"        self.occurence_counter += 1\n")
                fileHandle.write(f"        my_key = {self.classnames['Key']}({DictAsCall(self.keyParams)}, self.occurence_counter)\n")
            else:    
                fileHandle.write(f"        my_key = {self.classnames['Key']}({DictAsCall(self.keyParams)})\n")

            self.catch_duplicate_writer(fileHandle, "super().set(my_value,my_key)")
            if self.has_lang:
                fileHandle.write(f"        self._seen_languages[lang]=1\n")
            
        else:
            self.catch_duplicate_writer(fileHandle, "super().set(my_value)")
        fileHandle.write(f"\n")


    def catch_duplicate_writer(self, fileHandle, codeline:str) -> None:
        fileHandle.write(f"        try:\n")
        fileHandle.write(f"            {codeline}\n")
        fileHandle.write(f"        except Exception as e:\n")
        fileHandle.write(f"            msg = self._keyword + \":\" +str(e)\n")
        fileHandle.write(f"            raise type(e)(msg) from e\n")

    def get_and_has_value_writer(self, filehandle) -> None:
        if(self.classnames['Super'] == "_PxSingle"):
            filehandle.write(f"    def get_value(self) -> {DictAsReturntype(self.valueParams)}:\n")
            filehandle.write(f"        return super().get_value().get_value()")
        if len(self.keyParams) > 0:
            filehandle.write(f"    def get_value(self, {DictAsSignature(self.keyParams)}) -> {DictAsReturntype(self.valueParams)}:\n")
            if kw.is_duplicate_keypart_allowed:
                filehandle.write(f"        #TODO how should this function? Any usecases?\n")
                filehandle.write(f"        my_key = {self.classnames['Key']}({DictAsCall(self.keyParams)},1)\n")
            else:
                filehandle.write(f"        my_key = {self.classnames['Key']}({DictAsCall(self.keyParams)})\n")
            filehandle.write(f"        return super().get_value(my_key).get_value()")
        filehandle.write(f"\n\n")

        if(self.classnames['Super'] == "_PxSingle"):
            filehandle.write(f"    def has_value(self) -> bool:\n")
            filehandle.write(f"        return super().has_value()")
        if len(self.keyParams) > 0:
            filehandle.write(f"    def has_value(self, {DictAsSignature(self.keyParams)}) -> bool:\n")
            if kw.is_duplicate_keypart_allowed:
                filehandle.write(f"        #TODO how should this function? Any usecases?\n")
                filehandle.write(f"        my_key = {self.classnames['Key']}({DictAsCall(self.keyParams)},1)\n")
            else:
                filehandle.write(f"        my_key = {self.classnames['Key']}({DictAsCall(self.keyParams)})\n")
            filehandle.write(f"        return super().has_value(my_key)")
        filehandle.write(f"\n\n")        

            
    def get_lang_utils_writer(self, filehandle) -> None:
        if not self.has_lang:
            return
        
        filehandle.write(f"    def get_used_languages(self) -> list[str]:\n")
        filehandle.write(f"       return list(self._seen_languages.keys())\n\n")
        filehandle.write(f"    def reset_language_none_to(self,lang:str)->None:\n")
        filehandle.write(f"        if not lang:\n")
        filehandle.write(f"            return\n")
        filehandle.write(f"        if None in self.get_used_languages():\n")        
        filehandle.write(f"             super().reset_language_none_to(lang)\n")
        filehandle.write(f"             #unsee None\n")
        filehandle.write(f"             del self._seen_languages[None]\n")
        filehandle.write(f"             self._seen_languages[lang]=1\n")

# ---------------  end of class ----------------------------

class SpecReader:
    def __init__(self,) -> None:
       # read file
       with open("Keywords.csv", "r",encoding="utf-8-sig") as theSpecCsv:
         reader = csv.reader(theSpecCsv,delimiter=";" )
         header = next(reader)
         
         print(header)
         self.data = [MyKeyword(SpecRow(*row)) for row in reader] 

# ---------------  end of class ----------------------------

my_spec_reader = SpecReader()

# make <Keyword classes>.py
for kw in my_spec_reader.data:
    with open("../pxtool/model/keywords/"+kw.module_name+".py", "wt",encoding="utf-8-sig", newline="\n" ) as classPy:
        kw.imports_writer(classPy)
        kw.class_and_init_writer(classPy)
        kw.set_writer(classPy)
        kw.get_and_has_value_writer(classPy)
        kw.get_lang_utils_writer(classPy)

## model.keywords.

# make constants.py
mandatory_keys = []
langdependent_keys = []
content_indexed_keywords =[]
keyword_pythonic_map = {}

for kw in my_spec_reader.data:    
    keyword_pythonic_map[kw.keyword] = to_python_case(kw.keyword)
    if(kw.is_mandatory):
        mandatory_keys.append(to_python_case(kw.keyword))
    if(kw.has_lang):
        langdependent_keys.append(to_python_case(kw.keyword))
    if("content" in kw.subkeys_raw):
        content_indexed_keywords.append(to_python_case(kw.keyword))




with open("../pxtool/model/util/constants.py", "wt",encoding="utf-8-sig", newline="\n" ) as constant_module:
    constant_module.write("\"\"\"Module for holding constants\"\"\""+"\n\n")
    constant_module.write(f"MANDATORY_KEYWORDS = {str(mandatory_keys)}\n")
    constant_module.write(f"LANGDEPENDENT_KEYWORDS = {str(langdependent_keys)}\n")
    constant_module.write(f"CONTENT_INDEXED_KEYWORDS = {str(content_indexed_keywords)}\n")
    constant_module.write(f"KEYWORDS_PYTHONIC_MAP = {str(keyword_pythonic_map)}\n")

# make PxFileModel.py
myDict= {}
the_imports=[]
the_attributes = []
for kw in my_spec_reader.data:
    the_imports.append(f"from pxtool.model.keywords.{kw.module_name} import {kw.classnames['This']}")
    if kw.keyword == "DATA":
        the_attributes.append("self.unknown_keywords = \"\"")
    the_attributes.append(f"self.{to_python_case(kw.keyword)} = {kw.classnames['This']}()\n        \"\"\"{kw.px_comment}\"\"\"")
  
#from _PX_AXIS_VERSION import _PX_AXIS_VERSION
#
#self.axisversion = _PX_AXIS_VERSION()

with open("../pxtool/model/px_file_model.py", "wt",encoding="utf-8-sig", newline="\n") as model_py:
  #', '.join(kw.
  model_py.write("\n".join(the_imports)+"\n")
  model_py.write("from pxtool.model.util._px_super import _SuperKeyword\n\n")
  model_py.write("class PXFileModel:\n")
  model_py.write("    \"\"\"\n")
  model_py.write("    This class holds the information of a PxFile\n")
  model_py.write("    the setters have all value has first param, and stuff from the keyword-part after, because some of them are optional.\n")
  model_py.write("    \"\"\"\n\n")

  model_py.write("    def __init__(self) -> None:\n")
  model_py.write("        "+ "\n        ".join(the_attributes)+"\n\n")

  model_py.write("    def __str__(self):\n")
  model_py.write("        attrs = vars(self)\n")
  model_py.write("        attr_strings = [str(value) for value in attrs.values() if str(value) != \"\"]\n")
  model_py.write("        return \"\\n\".join(attr_strings)\n\n")

  model_py.write("    def get_attribute(self, name:str) -> _SuperKeyword:\n")
  model_py.write("        return getattr(self, name)\n")




######################################################################################

print("Done")









