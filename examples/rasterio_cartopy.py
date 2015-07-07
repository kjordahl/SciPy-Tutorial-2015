"""
Plot a raster image with Cartopy axes

Kelsey Jordahl
SciPy tutorial 2015
"""

import os
import numpy as np
import rasterio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

utm18n = ccrs.UTM(18)
ax = plt.axes(projection=utm18n)
plt.title('UTM zone 18N')


here = os.path.dirname(os.path.abspath('__file__'))
data_dir = os.path.join(here, '..', 'data')
raster_file = os.path.join(data_dir, 'manhattan.tif')


with rasterio.open(raster_file) as src:
    left, bottom, right, top = src.bounds
    a = np.ones((10, 10))
    ax.imshow(src.read(1), origin='upper',
              extent=(left, right, bottom, top), cmap='gray')
    x = [left, right, right, left, left]
    y = [bottom, bottom, top, top, bottom]
    ax.coastlines(resolution='10m', linewidth=4, color='red')
    ax.gridlines(linewidth=2, color='lightblue', alpha=0.5, linestyle='--')

plt.savefig('rasterio_cartopy.png', dpi=300)
plt.show()
