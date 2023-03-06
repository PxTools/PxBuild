from pxtool.loaders.loader_pxfile import Loader
from pxtool.model.px_file_model import PXFileModel
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

def test_statfin_khi_pxt_11xm_full_read_ok():        
        dummy = Loader('testdata/statfin_khi_pxt_11xm_full.px')
        model: PXFileModel = dummy.outModel
        assert "MADE-WITH=" in model.unknown_keywords