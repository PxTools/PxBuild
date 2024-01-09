import pytest
import pxbuild
from pxbuild.models.output.pxfile.px_file_model import PXFileModel
#import testdata.expected.test_data_03024 as expected


class TestCube1:
    def test_cube_1_ok(self):
      dummy = pxbuild.LoadFromPxmetadata('1', 'testdata/test_cube_1/test_config.json')
      

    #assert actual_data == expected.DATA


    


    