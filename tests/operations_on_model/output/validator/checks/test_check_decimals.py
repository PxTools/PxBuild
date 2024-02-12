from pxbuild.models.output.pxfile.px_file_model import PXFileModel
from pxbuild.operations_on_model.output.validator.checks.check_decimals import check_decimals


def test_check_decimals_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(7)

    val_rep = check_decimals(pxfile)
    assert not val_rep.is_valid
    assert (
        "Value <7> in decimals is not valid. When the keyword showdecimals is not specified, the value for decimals must be between 0 and 6."
        in val_rep.error_msg
    )


def test_check_decimals_is_valid():
    pxfile = PXFileModel()
    pxfile.decimals.set(5)

    val_rep = check_decimals(pxfile)
    assert val_rep.is_valid
