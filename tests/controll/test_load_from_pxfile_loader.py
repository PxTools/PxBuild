from pxbuild.controll.load_from_pxfile import Loader
from pxbuild.models.output.pxfile.px_file_model import PXFileModel
import pytest

class TestBadStart:
   def test_BadStart1_file_raises_value_error(self):
     with pytest.raises(ValueError, match="A PxFile must start with a letter"):
        dummy = Loader('testdata/BadFiles/BadStart1.px')

   def test_BadStart2_file_raises_value_error(self):
     with pytest.raises(ValueError, match="A PxFile must start with a letter"):
        dummy = Loader('testdata/BadFiles/BadStart2.px')  

   def test_BadStart3_file_raises_value_error(self):
     with pytest.raises(ValueError, match="A PxFile must start with a letter"):
        dummy = Loader('testdata/BadFiles/BadStart3.px')    

class TestQuoteUnquote:
   def test_QuoteUnquote1_file_raises_value_error(self):
     with pytest.raises(Exception, match="Hmm, there is something:wrongplacement1 between "):
        dummy = Loader('testdata/BadFiles/QuoteUnquote1.px')  

   def test_QuoteUnquote2_file_raises_value_error(self):
     with pytest.raises(Exception, match="Hmm, expected non-empty UnquotedItem."):
        dummy = Loader('testdata/BadFiles/QuoteUnquote2.px')          

class TestBadValues:
   def test_BadValueType1_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart AXIS-VERSION: Excepting single quoted string, but items has not len = 1"):
        dummy = Loader('testdata/BadFiles/BadValueType1.px')

   def test_BadValueType2_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart AGGREGALLOWED: Excepting single unquoted string YES or NO, but items has not len = 1"):
        dummy = Loader('testdata/BadFiles/BadValueType2.px')

   def test_BadValueType3_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart AGGREGALLOWED: Boolean values must be YES or NO, not"):
        dummy = Loader('testdata/BadFiles/BadValueType3.px') 

   def test_BadValueType4_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart DECIMALS: Excepting an integer as single unquoted string, but items has not len = 1"):
        dummy = Loader('testdata/BadFiles/BadValueType4.px')

   def test_BadValueType5_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart DECIMALS: integer value convertion"):
        dummy = Loader('testdata/BadFiles/BadValueType5.px')   

   def test_BadValueType6_file_raises_value_error(self):
      with pytest.raises(Exception, match="Bad list"):
        dummy = Loader('testdata/BadFiles/BadValueType6.px')  

   def test_BadValueType7_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart LANGUAGES: List must start with quoted string"):
        dummy = Loader('testdata/BadFiles/BadValueType7.px')  

   def test_BadValueType8_file_raises_value_error(self):
     with pytest.raises(Exception, match="Value for keypart LANGUAGES: Bad list, at item-index1: expected comma found ."):
        dummy = Loader('testdata/BadFiles/BadValueType8.px')  

class TestValidFilesLoads:
   def test_statfin_khi_pxt_11xm_full_read_ok(self):        
        dummy = Loader('testdata/statfin_khi_pxt_11xm_full.px')
        model: PXFileModel = dummy.outModel
        assert "MADE-WITH=" in model.unknown_keywords

   def test_ok_odd_usage_read_ok(self):
      dummy = Loader('testdata/ok_odd_usage.px')