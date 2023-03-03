import sys
my = sys.path[0].replace("\\demo","\\")
sys.path.insert(1,my)
#from pxtool.model.px_file_model import PXFileModel
import pxtool

from pxtool.model.util.util import Util

#Utforskende nybegynner uvitende om PCAXIS
a = pxtool.model.px_file_model.PXFileModel()
a.axis_version.set("2023")

#a.title.set(titleText="Yxi Kaksi", lang="fi")
#a.title.set(value="Nice table", lang="en")

a.title.set("Yxi Kaksi", "fi")
a.title.set("Fin tabell")
a.tableid.set("123132") 
a.decimals.set(15)
a.languages.set(["no","en","fi"])
a.language.set("no")


a.codes.set(codes=["c1","c2","c3"],variable="var_c")
a.codes.set(codes=["c1","c2","c4"],variable="var_d")
#a.codes.set(["c1","c2","c4"],"var_d","no")

#CODES("var_c")="c1","c2","c3"
a.codes.set(codes=["c1","c2","c3"],variable="var_c",lang="en")
#CODES["en"]("var_c")="c1_en","c2_en","c3_en"  og da bør c1 = c1_en

a.precision.set(4,"var_c","c2","en")

a.partitioned.set(["part11","2"],"var_D","en")
a.partitioned.set(["part21","2"],"var_D","en")

a.timeval.set("A1",["2020","2021"],"tid")
a.aggregallowed.set(True)
a.stockfa.set("A",None,"no")


# data:


datastring="""
"......." "......." "......." "......." 
"......." "......." "......." "......." 
1.2 0.9 34161.0 29982.0 
"......." "......." "......." "......." 
"......." "......." "......." "......." 
0.8 1.7 12532.0 13361.0 
"......." "......." "......." "......." 
1.5 1.8 11632.0 11767.0 
"..." "..." "..." "..." 
0.1 0.1 13901.0 8916.0 
"..." "..." "..." "..." 
0.1 "..." 7779.0 "..." 
2.6 4.4 18678.0 25241.0 
"""


a.data.set( datastring.split())

#----



#Expert bruker:
#a.set(keyword="CODES",value=["01","02"],subkey=["region"],lang="fi")
#  def set(self, keyword: str,  value:List, subkey:list = None, lang: str = None) -> None:


#Kan også eksponere flere klasser, som man setter sammen til en modell:  
#variabel = new variabel("....)
#variabel.set noe
#model.AddVariable(variabel)

#print( type(a.codepage._px_value).__name__ )

print(a)
print("--------")

Util.apply_default_language(a)

print(a.codes.get_used_languages())

print(a)
