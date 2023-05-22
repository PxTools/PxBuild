from pxtool.operations_on_model.loaders.loader_pxfile import Loader
from pxtool.operations_on_model.refine.fix_the_variable_type_keyword import fix_the_variable_type_keyword
import pytest

def test_fix_the_variable_type_keyword_raises():
      dummy = Loader('testdata/clean_me.px')
      with pytest.raises(Exception, match="One of check_language, check_stub_and_heading, "):
          fix_the_variable_type_keyword(dummy.outModel)
 