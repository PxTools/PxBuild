import sys
my2 = sys.path[0].replace("\\tests","\\src")
sys.path.insert(1,my2)

print(f"sys.path 0:{sys.path[0]}")
print(f"sys.path 1:{sys.path[1]}")
print(f"sys.path 2:{sys.path[2]}")


#from pxtool.model import px_file_model
#vart = px_file_model.PXFileModel()

from pxtool.model.px_file_model import PXFileModel
vart = PXFileModel()


vart.axis_version.set("2002")
print(vart)

#from pxtool.model import PxFileModel
#from pxtool.model import PxFileModel

def test_fizz():
    assert "fizz" == "fizz"



