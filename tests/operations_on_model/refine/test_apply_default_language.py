from pxtool.operations_on_model.loaders.loader_pxfile import Loader

from pxtool.operations_on_model.refine.apply_default_language import apply_default_language
import pytest

def test_apply_default_language_ok():
      dummy = Loader('testdata/clean_me.px')
      apply_default_language(dummy.outModel)
      