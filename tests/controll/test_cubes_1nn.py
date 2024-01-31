import pytest
import filecmp
import os

import pxbuild

class TestCubes1nn:
    def set_path(self) -> None:
        #pytest dont like dunder init
        self._my_path = "testdata/test_cubes_1nn/"
        self._my_config= self._my_path + "config.json"
        self._path_expected = self._my_path + "/expected/"

    def get_actual_path(self,id:str) -> str:
         return "testdata/out_files/cubes_1nn/test_cube_{id}/".format(id=id)

    #101: missing row and value without symbol_columns
    #102: missing row and value with 1 symbol_column
    #103: missing row and value with 2 symbol_column
    #104: as 103 but shuffled csv rows and cols
    #130: as 103 but testing stupid columnnames in CSV
    #131: as 103 but testing stupid columnnames in CSV        

    def test_cube_101_ok(self):
      self.set_path()

      dummy = pxbuild.LoadFromPxmetadata('101', self._my_config)
      file = "tab_101.px"
      result = filecmp.cmp(self._path_expected + file, self.get_actual_path("101") + file, shallow=False)
      assert result, file + " is not as expected."   

    def test_cube_102_ok(self):
      self.set_path()
      dummy = pxbuild.LoadFromPxmetadata('102', self._my_config)
      file = "tab_102.px"
      result = filecmp.cmp(self._path_expected + file, self.get_actual_path("102") + file, shallow=False)
      assert result, file + " is not as expected."     

    def test_cube_103_ok(self):
      self.set_path()
      dummy = pxbuild.LoadFromPxmetadata('103', self._my_config)
      file = "tab_103.px"
      result = filecmp.cmp(self._path_expected + file, self.get_actual_path("103") + file, shallow=False)
      assert result, file + " is not as expected."

    def test_cube_104_ok(self):
      self.set_path()
      dummy = pxbuild.LoadFromPxmetadata('104', self._my_config)
      file = "tab_104.px"
      result = filecmp.cmp(self._path_expected + file, self.get_actual_path("104") + file, shallow=False)
      assert result, file + " is not as expected."   

    def test_cube_130_as_103_but_with_stupid_columnnames_csv(self):
      self.set_path()
      dummy = pxbuild.LoadFromPxmetadata('130', self._my_config)
      file = "tab_130.px"
      result = filecmp.cmp(self._path_expected + file, self.get_actual_path("130") + file, shallow=False)
      assert result, file + " is not as expected." 

    def test_cube_131_as_103_but_with_stupid_columnnames_parquet(self):
      self.set_path()
      dummy = pxbuild.LoadFromPxmetadata('131', self._my_config)
      file = "tab_131.px"
      result = filecmp.cmp(self._path_expected + file, self.get_actual_path("131") + file, shallow=False)
      assert result, file + " is not as expected." 
      



    


    