# These 3 lines are here since we are using files in the same repo, not from a package.   
import sys
my = sys.path[0].replace("\\demo","\\")
sys.path.insert(1,my)

print ("paths",sys.path[0],sys.path[1])

#Create empty model:
import pxtool

from pxtool.controll.datafile import ParquetDatasource
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd


asdas = pxtool.LoadFromPxmetadata('12576', "enum.LOCAL_FOLDER")
#asdas = pxtool.LoadFromPxmetadata('07459', "enum.LOCAL_FOLDER")
#asdas = pxtool.LoadFromPxmetadata('03024', "enum.LOCAL_FOLDER")
#asdas = pxtool.LoadFromPxmetadata('03024', API)

#filePath='example_data/parquet_files/output_file03024.parquet' 
#mparquet = ParquetDatasource(filePath)
#mparquet.DoIt()

