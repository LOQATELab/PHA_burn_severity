def dNBR(dir, dir2, band1, band2, plot=False):
    
    #Prefire NBR. 
    Prefire = rxr.open_rasterio(dir, masked=True)
    PreNIR = Prefire.sel(band=int(band1))
    PreSWIR = Prefire.sel(band=int(band2))
    PreNBR = (PreNIR - PreSWIR) / (PreNIR + PreSWIR)

    #Postfire NBR.
    Postfire = rxr.open_rasterio(dir2, masked=True)
    PostNIR = Postfire.sel(band=int(band1))
    PostSWIR = Postfire.sel(band=int(band2))
    PostNBR = (PostNIR - PostSWIR) / (PostNIR + PostSWIR)

    #Differenced NBR.
    dNBR = PreNBR - PostNBR

    if plot == True:
        dNBR.squeeze().plot.imshow(cmap = 'inferno')
    
    return dNBR


