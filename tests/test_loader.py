from pxtool.loaders.loader_pxfile import Loader
import pytest

def test_BadStart1_file_raises_value_error():
    with pytest.raises(ValueError, match="A PxFile must start with a letter"):
        dummy = Loader('testdata/BadFiles/BadStart1.px')

def test_BadStart2_file_raises_value_error():
    with pytest.raises(ValueError, match="A PxFile must start with a letter"):
        dummy = Loader('testdata/BadFiles/BadStart2.px')  

def test_BadStart3_file_raises_value_error():
    with pytest.raises(ValueError, match="A PxFile must start with a letter"):
        dummy = Loader('testdata/BadFiles/BadStart3.px')    


