"""
Run this file to download and install the data files for the geospatial
tutorial.

If you have already downloaded the file tutorial_data.zip, no need to
run this script. Just unzip that file and place the data folder in this
directory.

Kelsey Jordahl
SciPy 2015

"""

from __future__ import print_function

import os
import sys
from shutil import rmtree
import zipfile

# python 2/3 compatible imports
try:
    from StringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


url = 'http://public.enthought.com/~kjordahl/scipy2015/tutorial_data.zip'


if sys.version_info[0] < 3:
    input = raw_input

here = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(here, 'data')

if os.path.exists(data_dir):
    conf = input('data directory exists. Delete? [y/n]')
    if conf.upper() == 'Y':
        print('deleting existing directory.')
        rmtree(data_dir)
    else:
        sys.exit(1)

print('reading remote file {}'.format(url))
response = urlopen(url)
zf = zipfile.ZipFile(BytesIO(response.read()), 'r')
zf.extractall(here)
print('Done!')
