import sys
my = sys.path[0].replace("\\demo","\\")
sys.path.insert(1,my)

from pxtool.loaders.loader_pxfile import Loader
from pxtool.model.cleaner import Cleaner

#loader = Loader('testdata/testdataKort.px')
#loader = Loader('testdata/statfin_khi_pxt_11xm.px')
loader = Loader('testdata/statfin_khi_pxt_11xm_full.px')

Cleaner.apply_default_language(loader.outModel)

with open('output.txt', 'w') as f:
    print(loader.outModel, file=f)



