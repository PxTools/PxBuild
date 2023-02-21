import os
notebook_path = os.getcwd()
while ".gitignore" not in os.listdir():
    os.chdir("../")


if "src" in  os.listdir():
    print("src funnet")   
 
from src.pxtool.model import PxFileModel


def test_fizz():
    assert "fizz" == "fizz"

