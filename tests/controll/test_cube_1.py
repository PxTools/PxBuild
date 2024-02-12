import pxbuild


class TestCube1:
    def test_cube_1_dont_crash(self):
        pxbuild.LoadFromPxmetadata("1", "testdata/test_cube_1/test_config.json")
