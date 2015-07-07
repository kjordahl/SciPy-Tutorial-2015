#! /bin/bash
ENV_NAME=2015-geospatial
conda create --yes -n $ENV_NAME python=2  fiona shapely rasterio pandas basemap requests
conda install --yes -n $ENV_NAME -c ocefpaf rtree
conda install --yes -n $ENV_NAME -c asmeurer pyproj descartes
source activate $ENV_NAME
pip install git+git://github.com/geopandas/geopandas.git
pip install github3.py
pip install --no-deps geojsonio  # Use --no-peds to avoid downgrading six and github3.py
