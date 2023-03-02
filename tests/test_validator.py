from pxtool.model.px_file_model import PXFileModel
from pxtool.model.util.validate_px import ValidateMethods as val
import pytest


def test_validate_check_decimals_raises_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(7)
    with pytest.raises(ValueError, match=f"Value <7> in decimals is not valid. When the keyword showdecimals is specified the value for decimals must be between 0 and 6."):
        rep = val.check_decimals(pxfile)

def test_check_decimals_returns_OK():
    pxfile = PXFileModel()
    pxfile.decimals.set(5)

    assert val.check_decimals(pxfile) == "Decimal check complete."

def test_check_showdecimals_value_error():
    pxfile = PXFileModel()
    pxfile.decimals.set(2)
    pxfile.showdecimals.set(3)
    with pytest.raises(ValueError, match=f"Value <3> in showdecimals is not valid. The value must be less or equal decimals."):
        rep = val.check_showdecimals(pxfile)

def test_check_codes_values_equal_count_value_error():
    pxfile = PXFileModel()
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_c", lang="no")
    pxfile.codes.set(codes=["c1","c2","c3"],variable="var_d", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_c", lang="en")
    pxfile.codes.set(codes=["d1","d2","d3"],variable="var_d", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="no")
    pxfile.values.set(["v1","v2","v3"], variable="var_c", lang="en")

    with pytest.raises(ValueError, match=f"The combination for language 'en' and variable 'var_d' in codes is not defined for any values."):
        rep = val.check_codes_values_equal_count(pxfile)

def test_check_mandatory_returns_error():
    pxfile = PXFileModel()
    pxfile.title.set(title="TableTitle", lang="no")
    pxfile.decimals.set(2)
    pxfile.matrix.set(matrix="TestMatrix")

    with pytest.raises(ValueError, match=f"These kewywords are mandatory and is not set: SUBJECT-CODE, SUBJECT-AREA, DESCRIPTION, CONTENTS, UNITS, STUB, HEADING, VALUES, ATTRIBUTE-ID, ATTRIBUTE-TEXT, ATTRIBUTES, DATA"):
        rep = val.check_mandatory(pxfile)

