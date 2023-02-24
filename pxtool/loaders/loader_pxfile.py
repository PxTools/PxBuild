#from generated.PxFileModel.py import PxFileModel
import re
class QuotedItem:
    def __init__(self, string:str) -> None:
        self.string=string

    def hasPxPartSeparator(self) -> bool:
       return False

    def hasPxEndline(self) -> bool:
       return False
    
    def hasSubkeyStart(self) -> bool:
       return False
            
    def trimWhitespace(self) -> None:
        pass

    def __str__(self):
        return  f"QuotedItem in quotes:\"{self.string}\"" 

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
    def isEven(self,value:int) -> bool:
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
        print("    Valuepart")
        for item in items:
           print(f"      {item}")
        print("    --------")





    def __init__(self)-> None:
        self.currentKeyPart = None 
        with open('testdataKort.px', 'r') as file:
            file_contents = file.read()
        splitFileOnQuote = file_contents.split("\"")
        file=[]
        cnt=0
        for item in splitFileOnQuote:
            if self.isEven(cnt):
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



    
   

loader = Loader()






