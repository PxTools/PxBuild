# These 3 lines are here since we are using files in the same repo, not from a package.   
import sys
my = sys.path[0].replace("\\demo","\\")
sys.path.insert(1,my)

print ("paths",sys.path[0],sys.path[1])

#Create empty model:
import pxtool

asdas = pxtool.LoadFromPxmetadata('03024', "enum.LOCAL_FOLDER")
#asdas = pxtool.LoadFromPxmetadata('03024', API)