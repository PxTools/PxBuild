# These 3 lines are here since we are using files in the same repo, not from a package.
import sys
import pxbuild

my = sys.path[0].replace("\\demo", "\\")
sys.path.insert(1, my)

print("paths", sys.path[0], sys.path[1])

dummy = pxbuild.LoadFromPxmetadata("2", "testdata/test_cube_2/test_config.json")
# dummy = pxbuild.LoadFromPxmetadata('12576', 'example_data/pxbuildconfig/ssb_config.json')
# dummy = pxbuild.LoadFromPxmetadata('07459', 'example_data/pxbuildconfig/ssb_config.json')
# dummy = pxbuild.LoadFromPxmetadata('03024', 'example_data/pxbuildconfig/ssb_config.json')
# dummy = pxbuild.LoadFromPxmetadata('03024', API)
