from pxbuild.controll.load_from_pxfile import Loader
from pxbuild.models.output.pxfile.px_file_model import PXFileModel
import pytest


class TestBadStart:
    def test_badstart1_file_raises_value_error(self):
        with pytest.raises(ValueError, match="A PxFile must start with a letter"):
            Loader("testdata/BadFiles/BadStart1.px")

    def test_badstart2_file_raises_value_error(self):
        with pytest.raises(ValueError, match="A PxFile must start with a letter"):
            Loader("testdata/BadFiles/BadStart2.px")

    def test_badstart3_file_raises_value_error(self):
        with pytest.raises(ValueError, match="A PxFile must start with a letter"):
            Loader("testdata/BadFiles/BadStart3.px")


class TestQuoteUnquote:
    def test_quote_unquote1_file_raises_value_error(self):
        with pytest.raises(Exception, match="Hmm, there is something:wrongplacement1 between "):
            Loader("testdata/BadFiles/QuoteUnquote1.px")

    def test_quote_unquote2_file_raises_value_error(self):
        with pytest.raises(Exception, match="Hmm, expected non-empty UnquotedItem."):
            Loader("testdata/BadFiles/QuoteUnquote2.px")


class TestBadValues:
    def test_badvaluetype1_file_raises_value_error(self):
        with pytest.raises(
            Exception, match="Value for keypart AXIS-VERSION: Excepting single quoted string, but items has not len = 1"
        ):
            Loader("testdata/BadFiles/BadValueType1.px")

    def test_badvaluetype2_file_raises_value_error(self):
        with pytest.raises(
            Exception,
            match="Value for keypart AGGREGALLOWED: Excepting single unquoted string YES or NO, but items has not len = 1",
        ):
            Loader("testdata/BadFiles/BadValueType2.px")

    def test_badvaluetype3_file_raises_value_error(self):
        with pytest.raises(Exception, match="Value for keypart AGGREGALLOWED: Boolean values must be YES or NO, not"):
            Loader("testdata/BadFiles/BadValueType3.px")

    def test_badvaluetype4_file_raises_value_error(self):
        with pytest.raises(
            Exception,
            match="Value for keypart DECIMALS: Excepting an integer as single unquoted string, but items has not len = 1",
        ):
            Loader("testdata/BadFiles/BadValueType4.px")

    def test_badvaluetype5_file_raises_value_error(self):
        with pytest.raises(Exception, match="Value for keypart DECIMALS: integer value convertion"):
            Loader("testdata/BadFiles/BadValueType5.px")

    def test_badvaluetype6_file_raises_value_error(self):
        with pytest.raises(Exception, match="Bad list"):
            Loader("testdata/BadFiles/BadValueType6.px")

    def test_badvaluetype7_file_raises_value_error(self):
        with pytest.raises(Exception, match="Value for keypart LANGUAGES: List must start with quoted string"):
            Loader("testdata/BadFiles/BadValueType7.px")

    def test_badvaluetype8_file_raises_value_error(self):
        with pytest.raises(
            Exception, match="Value for keypart LANGUAGES: Bad list, at item-index1: expected comma found ."
        ):
            Loader("testdata/BadFiles/BadValueType8.px")


class TestValidFilesLoads:
    def test_statfin_khi_pxt_11xm_full_read_ok(self):
        dummy = Loader("testdata/statfin_khi_pxt_11xm_full.px")
        model: PXFileModel = dummy.outModel
        assert "MADE-WITH=" in model.unknown_keywords

    def test_ok_odd_usage_read_ok(self):
        Loader("testdata/ok_odd_usage.px")
