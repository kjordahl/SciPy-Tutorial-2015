"""
Test import of required and optional packages for SciPy 2015 tutorial

"""
from __future__ import print_function

import importlib
import sys


def import_version(pkg):
    try:
        mod = importlib.import_module(pkg)
        print(OK, '%s version %s' % (pkg, mod.__version__))
    except ImportError:
        print(FAIL, '%s not installed' % pkg)

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

print('Using python in', sys.prefix)
print(sys.version)

print()
print('Required packages:')

import_version('pyproj')
import_version('fiona')
import_version('shapely')
import_version('rasterio')
import_version('geopandas')

print()
print('Optional packages:')

try:
    import osgeo.gdal
    print(OK, 'GDAL version', osgeo.gdal.__version__)
except:
    print(FAIL, 'GDAL not installed')

try:
    from mpl_toolkits.basemap import __version__
    print(OK, 'Basemap version', __version__)
except ImportError:
    print(FAIL, 'Basemap not installed')


try:
    from cartopy import __version__
    print(OK, 'Cartopy version', __version__)
except ImportError:
    print(FAIL, 'Cartopy not installed')

try:
    import geojsonio
    print(OK, 'geojsonio installed')
except:
    print(FAIL, 'geojsonio not installed')
