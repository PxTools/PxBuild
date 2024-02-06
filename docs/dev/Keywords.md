
Keywords included in Round 1:
|px_keyword|source|comment|
|---------|---------|---------|
|CHARSET|conf||
|AXIS-VERSION|conf||
|CODEPAGE|conf||
|LANGUAGE|conf||
|LANGUAGES|conf||
|CREATION-DATE|conf|Just on/off. For easy file vs file diff in tests|
|FIRST-PUBLISHED|Meta||
|NEXT-UPDATE|stats||
|TABLEID|Meta||
|DECIMALS|Meta||
|SHOWDECIMALS|Meta||
|MATRIX|Meta||
|AGGREGALLOWED|Meta||
|SUBJECT-CODE|stats||
|SUBJECT-AREA|stats||
|COPYRIGHT|Meta||
|TITLE|Meta||
|DESCRIPTIONDEFAULT|Conf||
|CONTENTS|Meta||
|STUB|None||
|HEADING|None||
|CONTVARIABLE|Meta||
|VALUES|codes||
|CODES|codes||
|UNITS|Meta||
|DOUBLECOLUMN|Meta||
|PRESTEXT|Meta|labelConstructionOption|
|DOMAIN|Meta||
|VARIABLE-TYPE|Meta||
|ELIMINATION|Codes||
|PRECISION|Meta||
|LAST-UPDATED|Stats||
|CFPRICES|Meta||
|DAYADJ|Meta||
|SEASADJ|Meta||
|CONTACT|Stats||
|REFPERIOD|Meta||
|BASEPERIOD|Meta||
|SOURCE|Conf||
|OFFICIAL-STATISTICS|Meta||
|NOTEX|Meta|On table and on a coded dimention|
|NOTE|Meta|On table and on a coded dimention|
|VALUENOTEX|Meta and codes||
|VALUENOTE|Meta and codes||
|CELLNOTEX|Meta|CELLNOTE("\*","\*","Örebro", "1995")="Lekebergs kommun has been excluded from Örebro"|
|CELLNOTE|Meta||
|DATASYMBOL1|Conf||
|DATASYMBOL2|Conf||
|DATASYMBOL3|Conf||
|DATASYMBOL4|Conf||
|DATASYMBOL5|Conf||
|DATASYMBOL6|Conf||
|DATASYMBOLNIL|Conf||
|DATASYMBOLSUM|Conf||
|VARIABLECODE|Meta||
|META-ID|Stats and Meta (several places in Meta)||
|DATA|data||


Keyword that are not really implemented:
(remember output validation)
|px_keyword|comment||
|----|--|--|
|DATANOTE||3 keytypes table, variable and value. DATANOTE("VARIABLE","VALUE")="*", and then you it recomends to prefix your note/valuenote text with "\*", hmm pxweb knows there is a note/valuenote already, so why?|
|DATANOTECELL||DATANOTECELL("*", "20", "*", "BE0101F2", "*")="Ae" . Subkeys are from CODES. text(Ae) is presented with figure 56Ae(?).  Hmm, similar to attributes?|
|DATANOTESUM||What is the sum of 2 cells with DATANOTECELL|
|KEYS||There must be as many KEYSs as there are values in stub|
|ATTRIBUTE-ID|||
|ATTRIBUTE-TEXT|||
|ATTRIBUTES|||
|AUTOPEN||obsolete?|
|PX-SERVER||obsolete?|
|DIRECTORY-PATH||obsolete?|
|HIERARCHIES|||
|HIERARCHYLEVELS|||
|HIERARCHYLEVELSOPEN|||
|HIERARCHYNAMES|||
|DEFAULT-GRAPH||obsolete?|
|CONFIDENTIAL||obsolete?|
|PARTITIONED||obsolete?|
|ROUNDING||obsolete?|
|STOCKFA|| S (stock), F(flow) and A (average), examples?|
|MAP|||
|SURVEY|||
|LINK|||
|DATABASE|||
|INFOFILE|||
|INFO|||
|UPDATE-FREQUENCY||1)Do we need this if we have NEXT-UPDATE. 2) In big pdf this is languageless (indicates a codelist) and 256 chars (indicates not a codelist) .|
|SYNONYMS||issues/45|
|DESCRIPTION||Needed?|
|TIMEVAL||Needed?|

Comments/questions on keyword interpretation:
|px_keyword|comment||
|----|--|--|
|SYNONYMS||SYNONYMS is language independent. So there is room for improvment :-) |
|STOCKFA|| S (stock), F(flow) and A (average), examples?|
|UPDATE-FREQUENCY||1)Do we need this if we have NEXT-UPDATE. 2) In big pdf this is languageless (indicates a codelist) and 256 chars (indicates not a codelist) .|
|FIRST-PUBLISHED|Y|Big pdf:The date when the data cube was first published in the format CCYYMMDD hh:mm. Me: The first time a cube with this id was published or is this for revisions:The first time data for 2023 was pulished  |





