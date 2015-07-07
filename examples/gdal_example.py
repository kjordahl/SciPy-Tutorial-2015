"""
Read a raster file as a numpy array with GDAL

Author: Kelsey Jordahl, Enthought
Scipy 2015 geospatial tutorial

"""
import os
import matplotlib.pyplot as plt
from osgeo import gdal

# GDAL does not use python exceptions by default
gdal.UseExceptions()

here = os.path.dirname(os.path.abspath('__file__'))
data_dir = os.path.join(here, '..', 'data')
raster_file = os.path.join(data_dir, 'manhattan.tif')

geo = gdal.Open(raster_file)
drv = geo.GetDriver()
print(drv.GetMetadataItem('DMD_LONGNAME'))
img = geo.ReadAsArray()
print(img.shape)

plt.imshow(img[0,:,:], cmap='gray')
plt.show()
