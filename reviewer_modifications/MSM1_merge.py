#Load appropriate libraries.
import rasterio as rio
from rasterio.merge import merge
import os
import glob
import numpy as np

#Input and output paths.
#IDir = r'/Volumes/PhD/imagery/masters/output/MSM1/'
IDir = r'/Volumes/PhD/imagery/masters/output/MSM1_extended/'
ODir = r'/Volumes/PhD/imagery/masters/output/global/'


#Search terms and imagery grab
#sc = ['*12mmhr*', '*16mmhr*', '*20mmhr*', '*24mmhr*', '*28mmhr*', '*32mmhr*', '*36mmhr*', '*40mmhr*']
sc = ['*4mmhr*', '*8mmhr*', '*44mmhr*', '*48mmhr*', '*52mmhr*', '*56mmhr*', '*60mmhr*']
for x in sc:
    search_criteria = x
    RI = x.replace('*', '')
    raster_join = os.path.join(IDir, search_criteria)
    rasters = glob.glob(raster_join)

#Open imagery

    mosaic_files = []
    for file in rasters:
        image = rio.open(file)
        mosaic_files.append(image)
    mosaic, out_trans = merge(mosaic_files, nodata = 0)
    mosaic = np.where(mosaic == 0, np.nan, mosaic)

    out_meta = image.meta.copy()
    out_meta.update({
        "driver": "GTiff",
        "height": mosaic.shape[1],
        "width": mosaic.shape[2],
        "transform": out_trans,
        "crs": image.crs,
        "nodata": np.nan
    })
    name = f'{ODir}global_MSM1_{RI}.tif'
    with rio.open(name, "w", **out_meta) as dest:
        dest.write(mosaic)