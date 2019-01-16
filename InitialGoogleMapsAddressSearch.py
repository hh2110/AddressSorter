from functions import *
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gmplot import gmplot
import googlemaps
import random

# read in csv as df (with the first column as index_col)
data = pd.read_csv("./data/CleanPtData.csv", index_col=0)

# need to use googlemaps to find lat and loong of addresses
with open('api.txt') as f:
    myAPIkey=f.readline()
# set the api key first
gmaps_key=googlemaps.Client(key =myAPIkey)

# create empty Lon and Lat columns ... and google maps name
# geocode_object should be included too 
data["LAT"] = None
data["LON"] = None
data["GMAPS_NAME"] = None
data["GEOCODE_OBJECT"] = None
data["PARTIAL_RESULT"] = None

# find lat, lon for a random 50 addresses and add them to the dataFrame
chosen=random.sample(range(0, len(data)), 50)
chosen=range(0,len(data))
for i in chosen:
    geocode_result = gmaps_key.geocode(data['pntAddress'][i]+', Pakistan')
    if i%100==0:
        print(i)
        data.to_csv('./data/GMapsAddress_'+str(i)+'.csv')
    try:
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lon = geocode_result[0]["geometry"]["location"]["lng"]
        gname = geocode_result[0]["formatted_address"]
        gdata = geocode_result[0]
        partial = checkPartialMatch(geocode_result)
        data.iat[i, data.columns.get_loc("LAT")] = lat
        data.iat[i, data.columns.get_loc("LON")] = lon
        data.iat[i, data.columns.get_loc("GMAPS_NAME")] = gname
        data.iat[i, data.columns.get_loc("GEOCODE_OBJECT")] = gdata
        data.iat[i, data.columns.get_loc("PARTIAL_RESULT")] = partial
    except:
        gname = None
        lat = None 
        lon = None
        print("couldn't find address", i, data['pntAddress'][i])


#save the new dataframe that holds all the information
from datetime import datetime
time=datetime.now().strftime('%H%M')
data.to_csv('./data/GMapsAddress_'+time+'.csv')

