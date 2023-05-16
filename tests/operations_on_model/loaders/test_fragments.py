from pxtool.operations_on_model.loaders.loader_pxfile import Loader
from pxtool.model.px_file_model import PXFileModel
import pytest

class TestValidFilesLoadsNote:
   def test_Note_ok(self):        
        file_fragment = Loader('testdata/testdata_Note.px')
        model_fragment: PXFileModel = file_fragment.outModel

        assert len(model_fragment.note.get_used_languages()) == 3
        assert len(model_fragment.note._value_by_key) == 3
        for key in model_fragment.note._value_by_key:
            assert key.variable == None
            