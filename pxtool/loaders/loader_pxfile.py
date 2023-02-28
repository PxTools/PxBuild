import re
import pxtool

class QuotedItem:
    def __init__(self, string:str) -> None:
        self.string="\"\"\""+string+"\"\"\""

    def hasPxPartSeparator(self) -> bool:
       return False

    def hasPxEndline(self) -> bool:
       return False
    
    def hasSubkeyStart(self) -> bool:
       return False
            
    def trimWhitespace(self) -> None:
        pass

    def isTypeQuoted(self) -> bool:
       return True

    def __str__(self):
        return  f"QuotedItem in quotes:{self.string}" 

class UnQuotedItem:
    def __init__(self, string:str) -> None:
        self.string=string

    def hasPxPartSeparator(self) -> bool:
       return "=" in self.string

    def hasPxEndline(self) -> bool:
       return ";" in self.string   
    
    def hasSubkeyStart(self) -> bool:
       return "(" in self.string   
    
    def get_before_and_after(self,split_char:str) -> tuple:
        string1, _, string2 = self.string.partition(split_char)
        return string1, string2
    
    def trimWhitespace(self) -> None:
        self.string = trimmed_string = re.sub(r"\s+", "", self.string)

    def isTypeQuoted(self) -> bool:
       return False    

    def __str__(self):
        return  f"UnQuotedItem:{self.string}"    

class Keypart:
    keyword:str
    language:str
    subKeys:list[str]
    modelAttributeName:str
    

    def __init__(self, keyword:str, language:str, subKeys:list[str]) -> None:
        self.keyword = keyword
        self.language = language
        self.subKeys = subKeys
        self.modelAttributeName = keyword.replace("-", "_").lower()

    def __str__(self):
         langPart = f"[\"{self.language}\"]" if self.language else ""
         subkeyPart = "(\"" + "\",\"".join(self.subKeys) +"\")" if self.subKeys else ""
         return  f"{self.keyword}{langPart}{subkeyPart}"    
        
    

class Loader:
    def isEven(value:int) -> bool:
        if value % 2 == 0:
            return True
        else:
            return False
        
    def fixKeypart(self,items:list) -> None:
        #keypart:
        #KEYWORD[lang]( quotedsubkeys sep by ",")
        #only KEYWORD ismandatory
        #lang may be quoted

        print("    Keypart:")
        for item in items:
           item.trimWhitespace()
           print(f"      Debug:{item}")

        #split items into before and after start subkey 
        itemsBeforeSubkey=[]
        itemsAfterSubkey=[]
        foundSubkey = False
        for item in items:
           if item.hasSubkeyStart():
               stringBefore, stringAfter = item.get_before_and_after('(')
               if stringBefore:
                      itemsBeforeSubkey.append(UnQuotedItem(stringBefore))
               if stringAfter: 
                   raise Exception(f"Hmm, there is something :{stringAfter} between ( and \") in keypart.")
               foundSubkey = True
           else:
               if foundSubkey:
                  itemsAfterSubkey.append(item)
               else:
                   itemsBeforeSubkey.append(item)

        subKeys = [x.string for x in itemsAfterSubkey if isinstance(x, QuotedItem)]

        #The spec in unclear on  if both ["en"] and [en]  is allowed.
        #first item will be UnQuoted and will contain the "[" if language is present in the keypart.
        keyword=""
        langValue=""
        if isinstance(itemsBeforeSubkey[0], QuotedItem):  
            raise Exception(f"Hmm, expected UnquotedItem")
        else:
            if"[" in itemsBeforeSubkey[0].string:
                keyword, stringAfter = item.get_before_and_after('[')
                if "]" in stringAfter:  #stringAfter must be en]
                    langValue = stringAfter[:2]
                else:
                    langValue = itemsBeforeSubkey[1].string
            else:
                keyword = itemsBeforeSubkey[0].string

        self.currentKeyPart = Keypart(keyword,langValue,subKeys)
        print(self.currentKeyPart)
        print("    --------")

    def fixValuePart(self,items:list) -> None:
        attrName = self.currentKeyPart.modelAttributeName
        print(f"    Valuepart for {attrName}")
        myAttri = vars(self.outModel)[attrName]


        outLangPart = "" 
        outSubkeyPart = "" 
        if len(self.currentKeyPart.subKeys) > 0:
            outSubkeyPart=f", {', '.join(self.currentKeyPart.subKeys)}"

        outValue =""

        do_run_exec = True

        if myAttri.pxvalue_type == "_PxString":
            if len(items) != 1:
                 raise ValueError(f"Excepting single quoted string, but items has not len = 1 ")
            outValue=items[0].string
        elif myAttri.pxvalue_type == "_PxBool":
            if len(items) != 1:
                raise ValueError(f"Excepting unsingle quoted string YES or NO, but items has not len = 1")
            outValue="True"
            if items[0].string not in ["YES","NO"]:
                raise ValueError(f"Boolean values must be YES or NO")
            if  items[0].string == "NO":
                outValue="False"
        elif myAttri.pxvalue_type == "_PxInt":
            if len(items) != 1:
                raise ValueError(f"Excepting an integer as single unquoted string, but items has not len = 1")
            
            if not items[0].string.isdecimal():
                raise ValueError(f"integer value convertion")
            
            outValue="False"        
        elif myAttri.pxvalue_type == "_PxStringList":
            print("Stringlist")
            if Loader.isEven(len(items)):
                raise ValueError(f"Bad list")
            if not items[0].isTypeQuoted:
                raise ValueError(f"List must start with quoted string")
            
            myStrings=[]
            for idx, x in enumerate(items):
                if Loader.isEven(idx):
                    myStrings.append(x.string)
                elif x.string != ",":
                    raise ValueError(f"Bad list")
                
            outValue = "[" + ",".join(myStrings) + "]"

            for item in items:
                print(f"      {item}")
            print("    --------")
        elif myAttri.pxvalue_type == "_PxTlist":
            # TLIST(A1, ”1994”-”1996”);  or TLIST(A1), ”1994”, ”1995”,"1996”;
            firstItem = items.pop(0)
            tmp= firstItem.string.replace("TLIST(","").strip()
            timescale=tmp[0:2]

            outValue=f"\"{timescale}\", "

            if len(items) > 2 and items[1].string.strip() == "-":
                 outValue = outValue + f"{items[0].string} ,\"-\", {items[2].string}"
            else:
                outValue = outValue + "["
                for item in items:
                    outValue = outValue + item.string
                outValue = outValue + "]"
        elif myAttri.pxvalue_type == "_PxData":
            data_list=[]
            for item in items:
                data_list.append(item.string)
            self.outModel.data.set(data_list)
            do_run_exec = False

            
            
        if do_run_exec:
            string_to_exec = f"self.outModel.{attrName}.set({outValue}{outSubkeyPart}{outLangPart})"
            print("do_exec:" + string_to_exec)
            exec(string_to_exec)


        #    myAttri.set(myBool) 

        print(f"---- etter keyword {self.currentKeyPart}  er modellen ----")
        print(self.outModel) 

        print("--------")

    def __init__(self, filename:str)-> None:
        self.outModel = pxtool.model.px_file_model.PXFileModel()
        self.currentKeyPart = None 
        with open(filename, 'r') as file:
            file_contents1 = file.read()

        file_contents2 =  file_contents1.replace("\"\n\"","")
        splitFileOnQuote = file_contents2.split("\"")
        file=[]
        cnt=0
        for item in splitFileOnQuote:
            if Loader.isEven(cnt):
               file.append(UnQuotedItem(item))
            else:
               file.append(QuotedItem(item))
            cnt +=1

        current=[]
        collectingKey=True

        while len(file) > 0:
            item = file.pop(0)
            print (f"item:{item}")
            if collectingKey: 
                #item  remove all whitespace
                if not item.hasPxPartSeparator():
                   current.append(item)
                else:
                    stringBefore, stringAfter = item.get_before_and_after('=')
                    if stringBefore:
                      current.append(UnQuotedItem(stringBefore))
                    if stringAfter:
                        # put the "unused" part of the string back 
                        file.insert(0,UnQuotedItem(stringAfter))
                                  
                    self.fixKeypart(current)
                    collectingKey = False
                    current=[]
            else:
                #collection Valuepart
                if not item.hasPxEndline():
                   current.append(item)
                else:
                    stringBefore, stringAfter = item.get_before_and_after(';')
                    if stringBefore:
                      current.append(UnQuotedItem(stringBefore))
                    if stringAfter:
                        # put the "unused" part of the string back 
                        file.insert(0,UnQuotedItem(stringAfter))
                    self.fixValuePart(current)
                    collectingKey = True
                    current=[]



    







