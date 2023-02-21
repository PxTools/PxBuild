import csv
from collections import namedtuple

def DictAsSignature(inDict:dict) -> str:
    """Returns a dict as string in method signature (mystring:str, myint:int)"""
    return ', '.join(['{}:{}'.format(k, v) for k, v in inDict.items()])

def DictAsCall(inDict:dict) -> str:
    """Returns a dict as string in method call (mystring, myint)"""
    return ', '.join(inDict.keys())

def to_python_case(text):
    return text.replace("-", "_").lower()

def getKeyType(has_lang:bool,subkeys:dict,multi:bool) -> str:
       myOut = "" 
       if len(subkeys) > 0:
        myOut += "_" + "_".join(subkeys.keys())
       if has_lang:
        myOut += "_lang"
       if multi:
         myOut += "_multi"
       if myOut :  
         myOut ="_keytype"+myOut  
       return myOut


SpecRow = namedtuple("SpecRow", ['px_keyword', 'is_lang_dependent', 'is_Mandatory', 'px_SubKey', 'is_SubKey_Optional', 'is_duplicate_keypart_allowed_', 'px_valuetype', 'px_valuetype_params', 'linevalidate', 'px_enumvalues', 'px_comment'] )

#Tja, de er jo python typer alle sammen. Så det er vel typen til parameter i set funksjonen vs den typen som lagres value i super klassen
#PxTypesByPythonTypes={"list[str]":"_PxStringList","str":"_PxString","bool":"_PxBool","int":"int"}
to_native_types={"_PxStringList":"list[str]","_PxString":"str","_PxBool":"bool","int":"int","_PxData":"list"}

#contains list of validation method-stubs for valueTypes. The keyWord and inputvalue is added in generation. 
valuetype_line_val = {"_PxStringList":["is_not_None(","is_list_of_strings("],"_PxString":["is_not_None(","is_string("],"_PxBool":["is_not_None(","is_bool("],"int":["is_not_None(","is_int("]}


class MyKeyword:
    def __init__(self,csvRow:SpecRow) -> None:
        self.keyword = csvRow.px_keyword
        self.has_lang = bool(csvRow.is_lang_dependent)
        self.is_mandatory = bool(csvRow.is_Mandatory)  #todo
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
        self.classnames["This"] = "_PX_"+self.keyword.replace('-','_') 
        self.classnames["Value"]= self.px_valuetype
        self.classnames["Key"] = getKeyType(self.has_lang,self.subkeys,self.is_duplicate_keypart_allowed)
        self.classnames["Super"]= "_PXValueByKey" if self.has_lang else "_PXSingle"

       #Constructors



    #Writers

    def imports_writer(self, fileHandle) -> None:
        my_import = [self.classnames["Super"]]
        if self.classnames["Value"] != "int" :
             my_import.append( self.classnames["Value"] )
        fileHandle.write(f"from _px_super import {', '.join(my_import)}\n")
        if self.classnames["Key"]:
            fileHandle.write(f"from _px_keytypes import { self.classnames['Key']}\n")
        fileHandle.write("from _line_validator import LineValidator\n\n")


    def class_and_init_writer(self, fileHandle) -> None:
        fileHandle.write(f"class {kw.classnames['This']}({kw.classnames['Super']}): \n")
        if kw.is_duplicate_keypart_allowed:
            #the others use init in super  
            fileHandle.write(f"    def __init__(self, keyword:str) -> None:\n")
            fileHandle.write(f"        super().__init__(keyword)\n")
            fileHandle.write(f"        self.occurence_counter = 0\n")
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
        else:
            self.catch_duplicate_writer(fileHandle, "super().set(my_value)")

    def catch_duplicate_writer(self, fileHandle, codeline:str) -> None:
        fileHandle.write(f"        try:\n")
        fileHandle.write(f"            {codeline}\n")
        fileHandle.write(f"        except Exception as e:\n")
        fileHandle.write(f"            msg = self._keyword + \":\" +str(e)\n")
        fileHandle.write(f"            raise type(e)(msg) from e\n\n")

# ---------------  end of class ----------------------------

# read file
with open("Keywords.csv", "r",encoding="utf-8-sig") as theSpecCsv:
    reader = csv.reader(theSpecCsv,delimiter=";" )
    header = next(reader)
    print ("De to under bør være like")
    print("['px_keyword', 'is_lang_dependent', 'is_Mandatory', 'px_SubKey', 'is_SubKey_Optional', 'is_duplicate_keypart_allowed_', 'px_valuetype', 'px_valuetype_params', 'linevalidate', 'px_enumvalues', 'px_comment']")
    print(header)
    data = [MyKeyword(SpecRow(*row)) for row in reader] 


# make <Keyword classes>.py
for kw in data:
    with open("generated/"+kw.classnames['This']+".py", "wt",encoding="utf-8-sig") as classPy:
        kw.imports_writer(classPy)
        kw.class_and_init_writer(classPy)
        kw.set_writer(classPy)


# make PxFileModel.py
myDict= {}
the_imports=[]
the_attributes = []
for kw in data:
    the_imports.append(f"from {kw.classnames['This']} import {kw.classnames['This']}")
    the_attributes.append(f"self.{to_python_case(kw.keyword)} = {kw.classnames['This']}(\"{kw.keyword}\")")
  
#from _PX_AXIS_VERSION import _PX_AXIS_VERSION
#
#self.axisversion = _PX_AXIS_VERSION("AXIS-VERSION")

with open("generated/PxFileModel.py", "wt",encoding="utf-8-sig") as model_py:
  #', '.join(kw.
  model_py.write("\n".join(the_imports)+"\n\n")
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
  model_py.write("        return \"\\n\".join(attr_strings)\n")







          


a = int("3")
print(a)









