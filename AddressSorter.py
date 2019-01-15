from functions import *
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gmplot import gmplot
import googlemaps
import random

# read in csv as df (with the first column as index_col)
data = pd.read_csv("./data/Jan19_SH.csv", index_col=0)

# remove unwanted columns
unwanted=['opdhVbp', 'vstId', 'vstDate', 'opdhVpulse',
          'opdhVtemp', 'opdhDhtn', 'opdhDihd', 'opdhDhyper',
          'pntAge', 'opdhVbmi', 'opdhVheight', 'opdhVweight',
          'opdhDdm', 'vstAmount', 'vsrcId']
data.drop(unwanted, inplace=True, axis=1)
# inplace=true tells pd to make the changes in our object
# axis=1 - dropping columns

# check for empty cells and replace with 'Pakistan' (default)
print('number of empty cells', data.isnull().sum())
data['pntAddress']=data['pntAddress'].fillna('Pakistan')
print('number of empty cells after fillna', data.isnull().sum(), '\n')

# check the types of data in the addresses column
print('type of data in the df ', data.dtypes)
print('shape of dataFrame ', np.shape(data), '\n')

# need to use googlemaps to find lat and loong of addresses
with open('api.txt') as f:
    myAPIkey=f.readline()
# set the api key first
gmaps_key=googlemaps.Client(key =myAPIkey)

# create empty Lon and Lat columns ... and google maps name
data["LAT"] = None
data["LON"] = None
data["GMAPS_NAME"] = None

# find lat, lon for a random 50 addresses and add them to the dataFrame
chosen=random.sample(range(0, len(data)), 50)
for i in chosen:
    geocode_result = gmaps_key.geocode(data['pntAddress'][i]+', Pakistan')
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        gname = geocode_result[0]["formatted_address"]
        data.iat[i, data.columns.get_loc("LAT")] = lat
        data.iat[i, data.columns.get_loc("LON")] = lon
        data.iat[i, data.columns.get_loc("GMAPS_NAME")] = gname
    except:
        gname = None
        lat = None 
        lon = None
        print(i, data['pntAddress'][i])

# isloate the lon and lat data
latList=data["LAT"].values;
lonList=data["LON"].values;

# remove any None values for where lon and lat data could not be found
# or where address was not searched for
latList=latList[latList != np.array(None)]
lonList=lonList[lonList != np.array(None)]

# use gmap to create a heatmap and scatter graph of the addresses
gmap = gmplot.GoogleMapPlotter(33.99, 71.52, 12, apikey=myAPIkey)
gmap.heatmap(latList, lonList,
             threshold=100, radius=50, opacity=0.7,
             dissipating=True)
gmap.scatter(latList, lonList)
gmap.draw('HeatmapPlusScatter.html')

# on inspection of the html - the locations are not spread out 
# rather they are pinned at specific locations - for example, the
