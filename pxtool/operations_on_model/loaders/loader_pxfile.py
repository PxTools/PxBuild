import re
import pxtool
import pxtool.model.util.constants as constants

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
        self.string = re.sub(r"\s+", "", self.string)

    def isTypeQuoted(self) -> bool:
       return False    

    def __str__(self):
        return  f"UnQuotedItem:{self.string}"    

class Keypart:
    keyword:str
    language:str
    subKeys:list[str]

    def __init__(self, keyword:str, language:str, subKeys:list[str]) -> None:
        self.keyword = keyword
        self.language = language
        self.subKeys = subKeys
        

    def __str__(self):
         langPart = f"[{self.language}]" if self.language else ""
         subkeyPart = "(" + ",".join(self.subKeys) +")" if self.subKeys else ""
         return  f"{self.keyword}{langPart}{subkeyPart}" 
    

class Loader:
    def isEven(value:int) -> bool:
        if value % 2 == 0:
            return True
        else:
            return False

    def digest_keypart_valuepart_pair(self, key_items:list, value_items:list) -> None:
        keypart = self.getKeypart(key_items)
        if  keypart.keyword in constants.KEYWORDS_PYTHONIC_MAP.keys(): 
            self.fixValuePart(keypart, value_items)
        else:
            self.when_unknown_keyword(keypart, value_items)


    def getKeypart(self,items:list) -> Keypart:
        #keypart: KEYWORD[lang]( quotedsubkeys sep by ",")
        #only KEYWORD ismandatory, lang may be quoted

        #split items into before and after start subkey 
        itemsBeforeSubkey=[]
        itemsAfterSubkey=[]
        foundSubkey = False

        for item in items:
           item.trimWhitespace()
           if item.hasSubkeyStart():
               stringBefore, stringAfter = item.get_before_and_after('(')
               if stringBefore:
                      itemsBeforeSubkey.append(UnQuotedItem(stringBefore))
               if stringAfter: 
                   raise Exception(f"Hmm, there is something:{stringAfter} between ( and first \" in keypart.")
               foundSubkey = True
           else:
               if foundSubkey:
                  itemsAfterSubkey.append(item)
               else:
                   itemsBeforeSubkey.append(item)

        subKeys = [x.string for x in itemsAfterSubkey if x.isTypeQuoted()]

        #The spec in unclear on  if both ["en"] and [en]  is allowed.
        #first item will be UnQuoted and will contain the "[" if language is present in the keypart.
        keyword=""
        langValue=""
        if itemsBeforeSubkey[0].isTypeQuoted() or itemsBeforeSubkey[0].string =='' : 
            raise Exception(f"Hmm, expected non-empty UnquotedItem.")
        else:
            if"[" in itemsBeforeSubkey[0].string:
                keyword, stringAfter = itemsBeforeSubkey[0].get_before_and_after('[')
                if "]" in stringAfter:  #stringAfter must be: en]
                    langValue = "\"\"\"" + stringAfter[:2] + "\"\"\""
                else:
                    langValue = itemsBeforeSubkey[1].string
            else:
                keyword = itemsBeforeSubkey[0].string

        return Keypart(keyword,langValue,subKeys)


    def when_unknown_keyword(self,keypart:Keypart, valueitems:list) -> None:
        very_quoted_string=f"{keypart}={''.join([str(x.string) for x in valueitems])};"
        addString=very_quoted_string.replace("\"\"\"","\"")#.replace("\"\"","\"")
        # strings are """ quoted for strings with newline to survive in a exec

        if self.outModel.unknown_keywords: 
            self.outModel.unknown_keywords = self.outModel.unknown_keywords  + "\n" + addString
        else:
            self.outModel.unknown_keywords = addString

    def fixValuePart(self,keypart:Keypart, items:list) -> None:
        attrName = constants.KEYWORDS_PYTHONIC_MAP[keypart.keyword]
        print(f"    Valuepart for {attrName}")

        myAttri = vars(self.outModel)[attrName]
        # "MADE-WITH"

        outLangPart = "" 
        if keypart.language:
            outLangPart = f", {keypart.language}"

        outSubkeyPart = "" 
        if len(keypart.subKeys) > 0:
            outSubkeyPart=f", {', '.join(keypart.subKeys)}"

        outValue =""
        do_run_exec = True

        if myAttri.pxvalue_type == "_PxString":
            if len(items) != 1:
                 raise ValueError(f"Value for keypart {keypart}: Excepting single quoted string, but items has not len = 1 ")
            outValue=items[0].string
        elif myAttri.pxvalue_type == "_PxBool":
            if len(items) != 1:
                raise ValueError(f"Value for keypart {keypart}: Excepting single unquoted string YES or NO, but items has not len = 1")
            outValue="True"
            if items[0].string not in ["YES","NO"]:
                raise ValueError(f"Value for keypart {keypart}: Boolean values must be YES or NO, not:{items[0].string}")
            if  items[0].string == "NO":
                outValue="False"
        elif myAttri.pxvalue_type == "_PxInt":
            if len(items) != 1:
                raise ValueError(f"Value for keypart {keypart}: Excepting an integer as single unquoted string, but items has not len = 1")
            
            if not items[0].string.isdecimal():
                raise ValueError(f"Value for keypart {keypart}: integer value convertion")
            
            outValue="False"        
        elif myAttri.pxvalue_type == "_PxStringList":
            print("Stringlist")
            if Loader.isEven(len(items)):
                raise ValueError(f"Bad list")
            if not items[0].isTypeQuoted():
                raise ValueError(f"Value for keypart {keypart}: List must start with quoted string")
            
            myStrings=[]
            for idx, x in enumerate(items):
                if Loader.isEven(idx):
                    myStrings.append(x.string)
                else:
                    x.trimWhitespace()
                    if x.string != ",":
                        raise ValueError(f"Value for keypart {keypart}: Bad list, at item-index{idx}: expected comma found {x.string}")
                
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
                 outValue = outValue + f"{items[0].string} \"-\" {items[2].string}"
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


        print(f"---- etter keyword {keypart}  er modellen ----")
        print(self.outModel) 

        print("--------")

    def get_file_in_chunks(filename:str) -> list:
        """Reads file, removes any QuoteNewlineQuote, splits on quote and retuns the list with UnQuotedItem and QuotedItem  """
        my_out=[]

        with open(filename, 'r') as file:
            file_contents1 = file.read()

        firstChars=file_contents1[:2]
        if not firstChars.isalpha():
            raise ValueError(f"A PxFile must start with a letter. {filename} does not.") 

        file_contents2 =  file_contents1.replace("\"\n\"","")
        splitFileOnQuote = file_contents2.split("\"")
        
        unquoted = True
        for item in splitFileOnQuote:
            if unquoted:
               my_out.append(UnQuotedItem(item))
            else:
               my_out.append(QuotedItem(item))
            unquoted  = not unquoted

        return my_out
    

    def __init__(self, filename:str)-> None:
        self.outModel = pxtool.model.px_file_model.PXFileModel()

        file = Loader.get_file_in_chunks(filename)

        current_key_items=[]
        current_value_items=[]
        collectingKey=True

        while len(file) > 0:
            item = file.pop(0)
            print (f"item:{item}")
            if collectingKey:
                if not item.hasPxPartSeparator():
                   current_key_items.append(item)
                else:
                    stringBefore, stringAfter = item.get_before_and_after('=')
                    if stringBefore:
                      current_key_items.append(UnQuotedItem(stringBefore))
                    if stringAfter:
                        # put the "unused" part of the string back 
                        file.insert(0,UnQuotedItem(stringAfter))
                    collectingKey = False
            else:
                #collection Valuepart
                if not item.hasPxEndline():
                   current_value_items.append(item)
                else:
                    stringBefore, stringAfter = item.get_before_and_after(';')
                    if stringBefore:
                      current_value_items.append(UnQuotedItem(stringBefore))
                    if stringAfter:
                        # put the "unused" part of the string back 
                        file.insert(0,UnQuotedItem(stringAfter))


                    self.digest_keypart_valuepart_pair(current_key_items,current_value_items)

                    #get ready for next record 
                    collectingKey = True
                    current_key_items=[]
                    current_value_items=[]

        print(self.outModel)                 



    







