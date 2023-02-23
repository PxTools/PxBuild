import sys



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
    

    



