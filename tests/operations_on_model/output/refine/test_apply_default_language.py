from pxbuild.controll.load_from_pxfile import Loader
from pxbuild.operations_on_model.output.refine.apply_default_language import apply_default_language
import pytest

def test_apply_default_language_ok():
      dummy = Loader('testdata/clean_me.px')
      apply_default_language(dummy.outModel)
      assert dummy.outModel.subject_area.has_value("fi")
      