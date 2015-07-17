"""
Plot a raster image with Cartopy axes on a Mercator map.
This example reprojects the UTM image to Mercator.

Kelsey Jordahl
SciPy tutorial 2015
"""

import os
import rasterio
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

utm18n = ccrs.UTM(18)
merc = ccrs.Mercator()
ax = plt.axes(projection=merc)


here = os.path.dirname(os.path.abspath('__file__'))
data_dir = os.path.join(here, '..', 'data')
raster_file = os.path.join(data_dir, 'manhattan.tif')


with rasterio.open(raster_file) as src:
    left, bottom, right, top = src.bounds
    ax.set_extent((left, right, bottom, top), utm18n)
    ax.imshow(src.read(1), origin='upper', transform=utm18n,
              extent=(left, right, bottom, top), cmap='gray',
              interpolation='nearest')
    x = [left, right, right, left, left]
    y = [bottom, bottom, top, top, bottom]
    ax.coastlines(resolution='10m', linewidth=4, color='red')
    ax.gridlines(linewidth=2, color='lightblue', alpha=0.5, linestyle='--')

plt.savefig('rasterio_cartopy.png', dpi=300)
plt.show()
