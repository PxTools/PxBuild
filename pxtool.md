## Pxtool
Not everything here is true :-) but it illustrates how to think about the classes. 
There is about 80 Keywords.
There is one class responsible for the line(s) of each Keyword.
The PxFileModel has one of each of the "keyword"-classes

```mermaid
classDiagram

    PxFileModel *-- _Aggregallowed
    PxFileModel *-- _Languages
    PxFileModel *-- _Values
    PxFileModel *-- _Valuenote
    PxFileModel *-- _Variablecode
    
    <<Entrypoint>> PxFileModel
    <<Keyword_class>> _Aggregallowed
    <<Keyword_class>> _Languages
    <<Keyword_class>> _Variablecode
    <<Keyword_class>> _Values
    <<Keyword_class>> _Valuenote
    
```    
  


The logical lines/records in a pxfile have the form:

Keypart =  Valuepart ;

The keypart consist of 
- a Keyword 
- an optional 2 letter language code in [] (it may be quoted) 
- an optional "subcube pointer" which is one or more quoted strings separated by commas surounded by ()

like 
- AXIS-VERSION= ...
- NOTE\["en"\]= ...
- CODES\["en"\]("Year")= ...

The Keyword determins if language and subcube-pointer is allowed(/is needed/makes sence) Some keyparts may occur more than once, others may only occur once.
This also depends on the keyword.

So, the lines/keywords may be spilt in 2 groups: Those which "can be identifyed by just the Keyword, and the Others. 
To hold the other-than-keyword information a group of classes has been made. They start their name with Keytype.

The Valuepart also have different types like int and list of strings.

The "classes" I_Keytype and I_Valuetype exists only on a conceptual level. "Mutli" indicate that the Keypart may occur more than once (footnotes)  
```mermaid
classDiagram 
    _KeytypeLang --|> I_Keytype
    _KeytypeVariableLang --|> _KeytypeLang
    _KeytypeContentLang --|> _KeytypeLang
    _KeytypeVariableValueLang --|> _KeytypeLang
    _KeytypeVariableValue --|> I_Keytype
    _KeytypeVariableLangMulti --|> _KeytypeVariableLang
    _KeytypeVariableValueLangMulti --|> _KeytypeVariableValueLang
    _KeytypeValuesLangMulti --|> _KeytypeLang
    _KeytypeValuesMulti --|> I_Keytype
```    

```mermaid
classDiagram
    I_Valuetype <|-- _PxTlist
    I_Valuetype <|-- _PxHierarchy
    I_Valuetype <|-- _PxStringList
    I_Valuetype <|-- _PxString
    I_Valuetype <|-- _PxBool
    I_Valuetype <|-- _PxData
    I_Valuetype <|-- _PxInt
```
The "Keyword-classes" use 2 different superclasses, one \_PxSingle for those that have just the keyword and a value and \_PxValueByKey for the Others. 
```mermaid
classDiagram
   class _PXSingle{
     I_Valuetype _pxValue
   }

   class _PXValueByKey{
     -Dict(~I_Keytype~,~I_Valuetype~) _ValueByKey
   }

    _PXSingle *-- I_Valuetype
    _PXValueByKey *-- I_Valuetype
    _PXValueByKey *-- I_Keytype
   
    _PXSingle <|-- _Languages
    
    _PXValueByKey <|--_Valuenote
    
    <<Keyword_class>> _Languages
    <<Keyword_class>> _Valuenote

    
```  



      
