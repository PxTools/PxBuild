import sys
my = sys.path[0].replace("\\demo","\\")
sys.path.insert(1,my)

from pxtool.loaders.loader_pxfile import Loader

loader = Loader('testdata/testdata.px')