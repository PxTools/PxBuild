from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_mandatory import check_mandatory

import pytest


def test_check_mandatory_returns_error():
    pxfile = PXFileModel()
    pxfile.title.set(title="TableTitle", lang="no")
    pxfile.decimals.set(2)
    pxfile.matrix.set(matrix="TestMatrix")

    val_rep = check_mandatory(pxfile)
    assert val_rep.is_valid == False
    assert "These kewywords are mandatory and is not set" in val_rep.error_msg
