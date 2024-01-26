import pytest
import filecmp
import os

import pxbuild

class TestCubes2nn:
    def set_path(self) -> None:
        #pytest dont like dunder init
        self._my_path = "testdata/test_cubes_2nn/"
        self._my_config= self._my_path + "config.json"
        self._path_expected = self._my_path + "/expected/"
        self._path_actual = self._my_path + "/actual/"

    #200: many notes and metaid
  

    def test_cube_200_ok(self):
      self.set_path()
      dummy = pxbuild.LoadFromPxmetadata('200', self._my_config)
      file = "tab_200.px"
      result = filecmp.cmp(self._path_expected + file, self._path_actual + file, shallow=False)
      assert result, file + " is not as expected."   

    


    