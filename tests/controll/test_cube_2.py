import pytest
import filecmp
import os

import pxbuild

class TestCube2:
    def test_cube_2_ok(self):
      dummy = pxbuild.LoadFromPxmetadata('2', 'testdata/test_cube_2/test_config.json')

      path = "testdata/test_cube_2" 
      path_expected = path + "/expected/"
      path_actual = path + "/actual/"
      filelist = os.listdir(path_expected)

      for file in filelist:
           print(file)

           file_expected = path_expected + file
           file_actual = path_actual + file
           result = filecmp.cmp(file_expected, file_actual, shallow=False)

           assert result, file + " is not as expected."      


    


    