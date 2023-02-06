import csv
from collections import namedtuple

SpecRow = namedtuple("SpecRow", ['px_keyword', 'is_lang_dependent', 'is_Mandatory', 'px_SubKey', 'is_SubKey_Optional', 
'is_duplicate_keypart_allowed_', 'px_valuetype', 'px_enumvalues', 'px_comment'] )

with open("Keywords.csv", "r",encoding="utf-8-sig") as theSpecCsv:
    reader = csv.reader(theSpecCsv,delimiter=";" )
    header = next(reader)
    print(header)
   # SpecRow = namedtuple("SpecRow", header)

    data = [SpecRow(*row) for row in reader]  

    print(data[2].px_keyword)

dataDict = {}
for row2 in data:
    dataDict[row2.px_keyword] = row2
     







