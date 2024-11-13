import geopandas as gpd
import xarray as xr
import numpy as np
import rioxarray as rxr
import os
from math import e
import matplotlib.pyplot as plt

IDir = r'/Volumes/PhD/imagery/masters/output/dNBR'
ODir = r'/Volumes/PhD/imagery/masters/output/MSM1_extended/'


def MSM1(dnbr, 
          save=False):
    
    # Coefficients for Southern California
    b = -3.63
    b_1 = 0.41
    b_2 = np.array([0.67])
    b_3 = 0.7
    
    # File naming
    

    dnbr_flat = dnbr.values.flatten()
    pixarr = np.empty((dnbr_flat.shape[0]), dtype= float)
    pixarr[:] = np.nan
    x = np.where(np.isnan(dnbr_flat) == False)
        
    # Getting the data from dnbr_flat
    dnbrdata = dnbr_flat[x]
        
    # Pulling tif metadata
    metadata = dnbr.attrs
    x_1 = float(metadata.get('X1'))
    x_3 = float(metadata.get('X3'))
    s = np.multiply(dnbrdata, b_2)
    
    # s1 multiplication assumes when function is called that val is defined globally in code.
    
    # Per pixel analysis, probability stored in empty list p1
    R = [1.0, 2.0, 11.0, 12.0, 13.0, 14.0, 15.0]
    for val in R:
        s1 = np.multiply(s, val)
        p1 = []
        for i in s1:
            lnx =  b + (b_1 * x_1 * val) + i + (b_3 * x_3 * val)
            prob = (e ** lnx) / (1.0 + e ** lnx)
            p1.append(prob)
        
        # Append probability array, flatten data, reshape into image
        prob_arr = np.array(p1)
        p_final = prob_arr.flatten()
        pixarr[x] = p_final
        pixarrImg = pixarr.reshape((dnbr.shape[1], dnbr.shape[2]))
        out_dnbr = xr.Dataset()
        out_dnbr = xr.DataArray(pixarrImg, dims = ('y', 'x'),
                                coords = {'x': dnbr.coords['x'],
                                        'y': dnbr.coords['y']})
        out_dnbr = out_dnbr.where(~np.isnan(out_dnbr), np.nan)
        
        if save == True:
            outname = f"{basin}_MSM1_{int(val*4)}mmhr.tif"
            out_dnbr.rio.to_raster(os.path.join(ODir, outname), driver='GTIFF')


for filename in os.listdir(IDir):
    file = os.path.join(IDir, filename)
    basin = filename.split('_')
    basin = basin[1]
    image = rxr.open_rasterio(file)
    MSM1(image, True)