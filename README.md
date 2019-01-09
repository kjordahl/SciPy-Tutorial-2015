Geospatial Data with Open Source Tools in Python
================================================

This tutorial will focus on open source libraries that provide a high-level, pythonic interface to geographic data and computations. Students will learn to read standard GIS file formats, perform spatial calculations, and plot results.

Tutorial materials
------------------

- [Presentation slides](http://kjordahl.github.io/SciPy-Tutorial-2015)
- [Examples](examples)
- [Exercises](exercises)

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

`Fiona`, `Shapely`, and `pyproj` (as well as optional packages `GDAL`, `basemap` and `cartopy`) can be installed with the Canopy package manager, or from the command line using `enpkg`. Then follow the instructions for installing `rasterio` and `geopandas` with `pip` below.

### Installing with conda ###

Many of the packages are available in Anaconda. Matt Craig contributed the script [`conda-setup.sh`](conda-setup.sh) which installs all of the required packages (and most of the optional ones) for this tutorial.

### Installing with pip ###

First, make sure you are using the most recent version of `pip` available, either by updating from your distribution's package manager or by using `pip install --upgrade pip`.

For most of the packages, `pip install <packagename>` will be sufficient. Please install the most recent development version of `geopandas` with the command:

    pip install git+git://github.com/geopandas/geopandas.git

Alternatively, you can install the source package from the [geopandas GitHub repository](https://github.com/geopandas/geopandas) and install it into your python if you are comfortable doing so.

### Testing your installation ###

Run the [`check_env.py`](check_env.py) script. If all the required packages say `[ OK ]`, you should be ready.

Data
----

The data for this tutorial can be download at [this location](https://github.com/kjordahl/SciPy-Tutorial-2015/releases/download/v1.0/tutorial_data.zip). Please download and unzip this file in this directory. Alternatively, run the [`download_data.py`](download_data.py) script to handle the download and unpacking for you.
