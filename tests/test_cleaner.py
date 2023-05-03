from pxtool.loaders.loader_pxfile import Loader
from pxtool.model.px_file_model import PXFileModel
from pxtool.model.cleaner import Cleaner
import pytest

def test_clean_ok():
      dummy = Loader('testdata/clean_me.px')
      Cleaner.apply_default_language(dummy.outModel)
      