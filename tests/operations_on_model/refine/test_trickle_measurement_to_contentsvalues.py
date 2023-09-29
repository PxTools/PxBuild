from pxtool.controll.load_from_pxfile import Loader
from pxtool.operations_on_model.output.refine.trickle_measurement_to_contentsvalues import trickle_measurement_to_contentsvalues
import pytest

def test_trickle_measurement_to_contentsvalues_raises():
      dummy = Loader('testdata/clean_me.px')
      with pytest.raises(Exception, match="One of check_language, check_stub_and_heading, "):
          trickle_measurement_to_contentsvalues(dummy.outModel)
      