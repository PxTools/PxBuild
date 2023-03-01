import sys
my = sys.path[0].replace("\\demo","\\")
sys.path.insert(1,my)

from pxtool.loaders.loader_pxfile import Loader

#loader = Loader('testdata/testdataKort.px')
loader = Loader('testdata/statfin_khi_pxt_11xm.px')

