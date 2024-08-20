# SET IMAGE AND SHAPEFILE DIRECTORIES
import rasterio as rio
import rioxarray as rxr
import glob
import matplotlib.pyplot as plt


dirImgLoc = r'D:/imagery/masters/sentinel-2/S2B_MSIL2A_20171228T184749_N0500_R070_T11SKU_20230808T002939.SAFE/S2B_MSIL2A_20171228T184749_N0500_R070_T11SKU_20230808T002939.SAFE/GRANULE/L2A_T11SKU_A004243_20171228T184751/IMG_DATA/R20m/'
#dirImgLocPost = 'D:\imagery\masters\sentinel-2\S2B_MSIL2A_20171128T184719_N0500_R070_T11SKU_20230829T001221.SAFE\S2B_MSIL2A_20171128T184719_N0500_R070_T11SKU_20230829T001221.SAFE\GRANULE\L2A_T11SKU_A003814_20171128T184714\IMG_DATA\R20m\T11SKU_20171128T184719_B05_20m.jp2'

print(dirImgLoc)

NIR_path = glob.glob(dirImgLoc + '*B8A*')
SWIR_path = glob.glob(dirImgLoc + '*B12*')
print(NIR_path)
print(SWIR_path)


NIR = rxr.open_rasterio(NIR_path[0], masked=True)
SWIR = rxr.open_rasterio(SWIR_path[0], masked=True)

NBR = (NIR - SWIR) / (NIR + SWIR)
NBR.plot()
