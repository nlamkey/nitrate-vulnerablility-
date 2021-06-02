
# Nitrate Vulnerability Workflow
This repository is a workflow that processes in-situ nitrate-nitrite readings from a stream source and several types of raster data to determine sources and causes of nitrate-nitrite level fluctuations. 

This workflow is intended to supplement groundwater investigations that are concerned with stream-aquifer interactions. Conceptually, streams and phreatic aquifers exchange water and therefore chemical constituents. This exchange is difficult to quantify and sources and timing of chemical constituent fluctuations aren't always clear. Numerical groundwater flow models can simulate this exchange using background chemical readings, river stage and hydraulic head data but a numerical flow model is only as good as the conceptual model it is based off of. This workflow will provide a robust knowledge base that enhances the conceptual model and provides more detailed information on the inputs and variables supplied to a numerical flow model. 

This workflow aims to understand how some of the surficial processes expressed in remote sensing products (rasters) may or may not be correlated with nitrate-nitrite or other nutrient fluctuations. The final product is a raster containing classified areas where the degree of nitrate-nitrite level fluctuations are shown. 

# Data Requirements 

To run the workflow you will need the following data:

* MODIS Evapotranspiration (HDF)
* MODIS Phenology (HDF)
* PRISM precipitation and temperature (bil)
* gSSURGO gridded soil map (tif)
* Landsat (tif)
* 30m DEM (tif)
* Cropland data layer (tif)
* Landuse and landcover layer (tif)
* In-situ chemistry and discharge data (csv) 
* Model boundaries and site locations (shp)

# Notebooks

All required packages will be added to this repository and list of them will be generated here once the workflow is completed. Here are the ones you need to run the current notebook titled nitrate-study:
```python
import os
from glob import glob
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as sns
import rioxarray as rxr
import xarray as xr
import earthpy as et
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib import patches as mpatches, colors
import pyproj
import pylab
import sklearn
from sklearn.linear_model import LinearRegression
import earthpy.mask as em
import earthpy.plot as ep
```
This notebook introduces the AOI and processes Landsat data, chemistry data, and discharge data. The code creates plots of the chemistry and discharge data to assess how the nutrient in question behaves relative to discharge. The two major pieces of information derived are when nutrients enter the stream and whether or not they are coming from a subsurface source or surface source. 

The code also processes Landsat data to create a time series of NDVI. These data are fitted to a linear regression model to assess any immediate relationships with vegetation. 

# Running the Workflow

As of now there is one notebook that processes Landsat and chemistry data. You will need to clone the repository and run the code in Jupyter Notebook to use the workflow. 

To run the notebook you'll need to install the nitrate-vulnerability environment which is a version of the [earth analytics python environment](http://kufs.ku.edu/media/uploads/work/kars_report_96-1.pdf). To get the environment in this repo installed you can follow the instructions here: https://www.earthdatascience.org/workshops/setup-earth-analytics-python/

Once the environment is activated you'll need need to install the chem module in the python environment. To do this:

1) Navigate to the nitrate-vulnerability folder in bash

2)
```python

pip install -e .

from chem_module import chem_scripts as cs

```
Run the nitrate-study notebook first

Run the process-landsat-ndvi notebook second

Run the nitrate-ndvi-blog-post third



```python

```


