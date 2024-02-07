import sys
import pxbuild

my = sys.path[0].replace("\\demo", "\\")
sys.path.insert(1, my)

# from pxbuild.operations_on_model.loaders.loader_pxfile import Loader
# from pxbuild.operations_on_model.refine.apply_default_language import apply_default_language

# loader = Loader('testdata/testdataKort.px')
# loader = Loader('testdata/statfin_khi_pxt_11xm.px')
loader = pxbuild.Loader("testdata/statfin_khi_pxt_11xm_full.px")

# apply_default_language(loader.outModel)

with open("output.txt", "w") as f:
    print(loader.outModel, file=f)
