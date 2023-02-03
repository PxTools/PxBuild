import csv
from collections import namedtuple

with open("Keywords.csv", "r",encoding="utf-8-sig") as theSpecCsv:
    reader = csv.reader(theSpecCsv,delimiter=";" )
    header = next(reader)
    print(header)
    SpecRow = namedtuple("SpecRow", header)
    data = [SpecRow(*row) for row in reader]  



print("\n",data[3])







