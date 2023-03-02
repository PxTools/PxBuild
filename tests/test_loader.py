from pxtool.loaders.loader_pxfile import Loader
import pytest

def test_BadStart1_file_raises_value_error():
    with pytest.raises(ValueError):
        dummy = Loader('testdata/BadStart1.px')

def test_BadStart2_file_raises_value_error():
    with pytest.raises(ValueError):
        dummy = Loader('testdata/BadStart2.px')  

def test_BadStart3_file_raises_value_error():
    with pytest.raises(ValueError):
        dummy = Loader('testdata/BadStart3.px')    


