"""
Using GeoPandas to generate a vector mask and applying it to a raster image.

Kelsey Jordahl
SciPy tutorial 2015

"""

import rasterio
from rasterio.features import rasterize
from geopandas import read_file
import os
import matplotlib.pyplot as plt

here = os.path.dirname(os.path.abspath('__file__'))
data_dir = os.path.join(here, '..', 'data')

raster_file = os.path.join(data_dir, 'manhattan.tif')
vector_file = os.path.join(here, 'nybb_15b', 'nybb.shp')

df = read_file(vector_file)
plt.figure(1)


def show_img(img, bounds):
    left, bottom, right, top = bounds
    plt.imshow(img, cmap='gray', extent=(left, right, bottom, top))
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)

with rasterio.open(raster_file) as src:
    # extract Manhattan, transform coordinates and geometry only
    poly = df.to_crs(src.crs).ix[3]['geometry']
    coords = [p.exterior.coords.xy for p in poly]
    ax = plt.subplot(1, 2, 1)
    img = src.read(1)
    show_img(src.read(1), src.bounds)
    for x, y in coords:
        plt.plot(x, y, color='red', linewidth=2)
    ax.set_xlim(src.bounds.left, src.bounds.right)
    ax.set_ylim(src.bounds.bottom, src.bounds.top)
    plt.subplot(1, 2, 2)
    mask = rasterize([poly], transform=src.transform, out_shape=src.shape)
    # If we had opened the file with mode 'r!', we could write the mask
    # src.write_mask(mask)
    img[mask==0] = 255
    show_img(img, src.bounds)

plt.savefig('rasterize_mask.png', dpi=300)
plt.figure(2)
show_img(mask, src.bounds)
plt.savefig('mask.png', dpi=300)
plt.show()
