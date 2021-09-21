[![DOI](https://zenodo.org/badge/368717627.svg)](https://zenodo.org/badge/latestdoi/368717627)

# Nitrate Vulnerability Workflow
This repository is a workflow that processes in-situ nitrate-nitrite readings from a stream source and several types of raster data to determine sources and causes of nitrate-nitrite level fluctuations. 

This workflow is intended to supplement groundwater investigations that are concerned with stream-aquifer interactions. Conceptually, streams and phreatic aquifers exchange water and therefore chemical constituents. This exchange is difficult to quantify and sources and timing of chemical constituent fluctuations aren't always clear. Numerical groundwater flow models can simulate this exchange using background chemical readings, river stage and hydraulic head data but a numerical flow model is only as good as the conceptual model it is based off of. This workflow will provide a robust knowledge base that enhances the conceptual model and provides more detailed information on the inputs and variables supplied to a numerical flow model. 

This workflow aims to understand how some of the surficial processes expressed in remote sensing products (rasters) may or may not be correlated with nitrate-nitrite or other nutrient fluctuations in surface water. The workflow is data mining exercise that attempts to pull out patterns of hysteresis in high resolution chemical and discharge data and classified pixels based on k-means clustering analysis.

# Data Requirements 

To run the workflow you will need the following data:

* MODIS Evapotranspiration (HDF)
* PRISM precipitation and temperature (bil)
* Landsat (tif)
* 30m DEM (tif)
* Cropland data layer (tif)
* Landuse and landcover layer (tif)
* In-situ chemistry and discharge data (csv) 
* Model boundaries and site locations (shp)

# Data Access
All of the 160 Gigs of data for this workflow were acquired manually and processed on an external drive. If you'd like to use the same data contact me at nclamkey@gmail.com and I can post them on a temporary FTP site otherwise you can use the site AOI shapefile to get the extents and download the data from sources listed below. Plans to move this workflow to Google Earth Engine are underway.

## Prism 
https://prism.oregonstate.edu/recent/
## DEM 
https://apps.nationalmap.gov/downloader/#/
## Landsat and MODIS ET
https://earthexplorer.usgs.gov/
## Landuse and landcover
https://www.mrlc.gov/viewer/
## Cropland data layer
https://www.nass.usda.gov/Research_and_Science/Cropland/Release/
## Nitrate Data
https://waterdata.usgs.gov/sd/nwis/uv/?site_no=06481000&PARAmeter_cd=00630,99124,00631,99133,99137


# File structure of repo

All the shapefile and chemistry data are located in the data folder. This is also where the outputs of everything but the raster data live. 

The notebooks folder contains all the code to run the workflow. 

There is a powerpoint in the presentation folder for a quick overview what to expect. 

# File structure for code 

The file structure for this workflow isn't generated programmatically, yet. You will have to create the file structure and add your data there. The outputs are not generated automatically yet either so you will have to create folders for each output.  

# Install the Environment 

This notebook uses the earth analytics conda environment. To install this fork and clone the repository from [github](https://github.com/earthlab/earth-analytics-python-env). Then cd to the earth-analytics-python-env folder. Then run the following command:
```python
conda env create -f environment.yml
```

# Install the Chem Module
Before you run any notebooks intall the chem_model

```python
pip install -e .
```

# Notebook Order

1. Run the create-dataset-for-matching.ipynb first. 


2. Run all the open-process notebooks. 


3. Run the k-means-analysis.ipynb


4. Run the final-plots.ipynb 


5. Run the ea-final-blog-post-w5.ipynb


# The create-dataset-for-matching notebook
The notebooks that process raster data use an output created in the create-dataset-for-matching.ipynb. This is for rioxarray.reproject_match(). The output is a raster created from the prism precipitation data. This was an arbitrary choice feel free to set the data paths to any dataset. 

# The open-process notebooks
These notebooks will create as many output files as input files. The out put is tif with the same resolution and specs as you make the matching dataset. As is, the output is a 500m resolution tif in the ESPG: 26914 coordinate system. It's up to you where you want them to go. You'll have to set the paths to folder you make. 

Be warned the MODIS and Landsat notebooks are the most computation intensive. 

# The k-means-analysis notebook

The k-means clustering analysis isn't perfect. The raster processing notebooks need to have code added that removes any rasters with nan values to some threshold. That should improve the analysis a bit. I'm open to any suggestions. The inputs of this notebook are all the tifs produced by the open-process notebooks. 

The outputs of the notebook are a figure for the blog post. 

# The final-plots notebook

This notebook imports a shapefile containing the new extents to pull raster data from for the final plots. Because of the messy nature of ecological work, I exported the final cluster plot from the k-means-analysis notebook and made a manual interpretation of the part of the cluster I thought was most likely influencing the nitrate sensor location. I did this using QGIS.

With further refinement of the code, a programmatic way should be implemented.

# The final blog post notebook
The final blog post notebook will generate a blog post containing two of the figures from this workflow. 

# Code Failures 
You can run any of the open-process notebooks and run the the k-means-analysis notebook and produce results. Most code failures will be memory related. 


