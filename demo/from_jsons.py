# These 3 lines are here since we are using files in the same repo, not from a package.
import sys

my = sys.path[0].replace("\\demo", "\\")
sys.path.insert(1, my)

print("paths", sys.path[0], sys.path[1])

import pxbuild

dummy = pxbuild.LoadFromPxmetadata("03024", "example_data/pxbuildconfig/ssb_config.json")
