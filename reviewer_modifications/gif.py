import pandas as pd
from PIL import Image
import glob
import os
import geopandas as gpd


#basin_path = r'/Volumes/PhD/imagery/masters/TF_basin-TPN/OneDrive_1_11-7-2024/TF_TP-basins.shp'
#basin_path = r'/Volumes/PhD/imagery/masters/TF_basin-TPN/TF_FP-basins.shp'
#basin_path = r'/Volumes/PhD/imagery/masters/TF_basin-TPN/TF_I_NE.shp'
basin_path = r'/Volumes/PhD/imagery/masters/TF_basin-TPN/TF_TN_Final-basins.shp'
#basin_path = r'/Volumes/PhD/imagery/masters/TF_basin-TPN/TF_FN-basins.shp'

basins = gpd.read_file(basin_path)
basins = basins['BASIN_ID']

path = r'/Volumes/PhD/imagery/masters/output/global/TPN-basins/'
out = r'/Volumes/PhD/imagery/masters/gif/True-Negative/'
def make_gif(frame_folder, n):
    frames = [Image.open(image) for image in b]
    frame_one = frames[0]
    frame_one.save(os.path.join(out, f"Basin_{basin}_{n}.gif"), format="GIF", append_images=frames,
               save_all=True, duration=200, loop=0)

for basin in basins:
    n = 'TN'
    b = glob.glob(f'{path}/*{basin}**TN.png')
    b.sort()
    make_gif(b, n)