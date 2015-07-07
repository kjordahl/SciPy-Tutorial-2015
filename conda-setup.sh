#! /bin/bash

ENV_NAME=2015-geospatial

conda config --add channels ioos

conda create -n $ENV_NAME --file req.txt python=2.7
