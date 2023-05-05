from pxtool.model.px_file_model import PXFileModel
from pxtool.model.keywords._language import _Language
from pxtool.operations_on_model.validator.validate_px import Valdidate
from pxtool.operations_on_model.loaders.loader_pxfile import Loader
from pxtool.operations_on_model.refine.apply_default_language import apply_default_language

import pytest

def test_valdidate_ok():
     big_ok_file = Loader('testdata/statfin_khi_pxt_11xm_full.px')
     big_ok_model = big_ok_file.outModel
     apply_default_language(big_ok_model)
     val = Valdidate(big_ok_model)

     assert val.is_valid()
     report = val.get_report()
     assert len(val.checks_ran) > 5 





def test_valdidate_exit_at_step1():
    pxfile = PXFileModel()
    pxfile.title.set(title="TableTitle", lang="no")
    pxfile.decimals.set(2)
    pxfile.matrix.set(matrix="TestMatrix")
    
    val = Valdidate(pxfile)
    report = val.get_report()
    assert len(val.checks_ran) == 1 



def test_valdidate_exit_at_step2():
     big_ok_file = Loader('testdata/statfin_khi_pxt_11xm_full.px')
     big_bad_model = big_ok_file.outModel
     apply_default_language(big_bad_model)
     big_bad_model.language = _Language()
     big_bad_model.language.set("dk")
    
     val = Valdidate(big_bad_model)

     assert len(val.checks_ran) == 2 

def test_valdidate_exit_at_step3():
     big_ok_file = Loader('testdata/statfin_khi_pxt_11xm_full.px')
     big_bad_model = big_ok_file.outModel
     apply_default_language(big_bad_model)
     big_bad_model.title.set("Should fail validation, as dk is not in languages.","dk")
    
     val = Valdidate(big_bad_model)

     assert len(val.checks_ran) == 3      


    




