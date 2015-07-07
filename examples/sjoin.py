"""
Using GeoPandas to do a spatial join between points and polygons

Kelsey Jordahl
SciPy tutorial 2015

"""

import os
import numpy as np
import matplotlib.pyplot as plt

from geopandas import GeoDataFrame, GeoSeries, read_file
from geopandas.tools import sjoin
from shapely.geometry import Point

here = os.path.dirname(os.path.abspath('__file__'))
data_dir = os.path.join(here, '..', 'data')

vector_file = os.path.join(here, 'nybb_15b', 'nybb.shp')

boros = read_file(vector_file)

xmin, ymin, xmax, ymax = boros.total_bounds
N = 1000
X = np.random.uniform(low=xmin, high=xmax, size=N)
Y = np.random.uniform(low=ymin, high=ymax, size=N)
points = GeoDataFrame(geometry=GeoSeries([Point(x, y) for x, y in zip(X, Y)]))
points.crs = boros.crs
joined = sjoin(points, boros, how='inner')
joined.geometry = joined.buffer(2000)

ax = plt.subplot(121)
boros.plot(column='BoroCode', categorical=True, axes=ax)
points.plot(axes=ax)
ax.set_aspect('equal')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
ax = plt.subplot(122)
joined.plot(column='BoroCode', categorical=True, axes=ax)
ax.set_aspect('equal')
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)

plt.tight_layout()
plt.savefig('sjoin.png', dpi=300)
plt.show()
