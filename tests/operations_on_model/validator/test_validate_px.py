from pxtool.model.px_file_model import PXFileModel
from pxtool.operations_on_model.validator.validate_px import Valdidate

import pytest

def test_valdidate():
    pxfile = PXFileModel()
    pxfile.title.set(title="TableTitle", lang="no")
    pxfile.decimals.set(2)
    pxfile.matrix.set(matrix="TestMatrix")
    
    val = Valdidate(pxfile)
    




