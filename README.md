Geospatial Data with Open Source Tools in Python
================================================

This tutorial will focus on open source libraries that provide a high-level, pythonic interface to geographic data and computations. Students will learn to read standard GIS file formats, perform spatial calculations, and plot results.

Installation
------------

The following packages will be required for this tutorial:

* [pyproj](https://pypi.python.org/pypi/pyproj)
* [Fiona](https://pypi.python.org/pypi/Fiona)
* [Shapely](https://pypi.python.org/pypi/Shapely)
* [rasterio](https://pypi.python.org/pypi/rasterio)
* [geopandas](https://github.com/geopandas/geopandas)

Optional packages that may be used in demonstrations, but not required for exercises, include:

* [basemap](https://pypi.python.org/pypi/basemap/1.0.2)
* [Cartopy](http://scitools.org.uk/cartopy)
* [geojsonio.py](https://github.com/jwass/geojsonio.py)

These packages have a number of prerequisites, including NumPy, pandas, matplotlib, and GDAL. I recommend starting with a standard scientific python distribution such as [Canopy](https://store.enthought.com) or [Anaconda](https://store.continuum.io/cshop/anaconda).

All packages are supported for Python 2.7 and recent versions of Python 3 (3.4 is recommended). Any of the 3 major platforms (Windows, OS X, and Linux) should work. Particularly on Windows, using precompiled packages when available will usually be much easier and less error-prone.

### Installing in Canopy ###

`Fiona`, `Shapely`, and `pyproj` (as well as option packages `basemap` and `cartopy`) can be installed with the Canopy package manager, or from the command line using `enpkg`. You should also install `GDAL`, as a prerequisite for `rasterio`. Then follow the instructions for installing `rasterio` and `geopandas` with `pip` below.

### Installing with pip ###

First, make sure you are using the most recent version of `pip` available, either by updating from your distribution's package manager or by using `pip install --upgrade pip`.

For most of the packages, `pip install <packagename>` will be sufficient. Please install the most recent development version of `geopandas` with the command:

    pip install git+git://github.com/geopandas/geopandas.git

Alternatively, you can install the source package from the geopandas GitHub repository and install it into your python if you are comfortable doing so.

### Testing your installation ###

Run the `check_env.py` script. If all the required packages say `[ OK ]`, you should be ready.

Data
----

Smaller data files will be in the `data` directory of this repository. I'll provide a link for larger binary files.
