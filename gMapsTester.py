from functions import *
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import Levenshtein as lev
from gmplot import gmplot
import googlemaps

# this script is checking how good the google maps 
#results are relative to the input 

# read in csv as df (with the first column as index_col)
data = pd.read_csv("./data/GMapsAddresses.csv", index_col=0)

# we need to conpare each gm_result with the input
# there is a choice in which words to compare in both 
#the input and the result
# to keep it simple we can compare all the input with the
#first two elements of the comma separated list of the output
#and note down the levenshtein distance - number of operations
#required to produce the same string - if the levenshtein distance
#is <4 for any word in the input (except peshawar,phase,numbers) 
#we can take that as a spelling error and 100% match otherwise we give a 0

#will need a new column measuring precision
data['PRECISION']=None
data['MATCHING']=None

counter=0
for index, row in data.iterrows():
    inp1=row['pntAddress']
    res1=row['GMAPS_NAME']
    if type(res1)==str: #ignoring NaN values
        sim=SimilarityBtwStrings(inp1, res1)
        counter+=sim
        if sim==1:
            data.iat[index, data.columns.get_loc('MATCHING')]=1
        else:
            data.iat[index, data.columns.get_loc('MATCHING')]=0

data=data.loc[data['MATCHING']==1]

# isloate the lon and lat data
latList=data["LAT"].values;
lonList=data["LON"].values;

# now we can plot the matches that have a lev distance < 2
# remove any None values for where lon and lat data could not be found
# or where address was not searched for
latList=latList[latList != np.array(None)]
lonList=lonList[lonList != np.array(None)]

# need to use googlemaps to find lat and loong of addresses
with open('api.txt') as f:
    myAPIkey=f.readline()
# set the api key first
gmaps_key=googlemaps.Client(key =myAPIkey)

# use gmap to create a heatmap and scatter graph of the addresses
gmap = gmplot.GoogleMapPlotter(33.99, 71.52, 12, apikey=myAPIkey)
gmap.heatmap(latList, lonList,
             threshold=1, radius=50, opacity=0.7,
             dissipating=True)
gmap.scatter(latList, lonList)
gmap.draw('HeatmapPlusScatterAccurate.html')

#save the new dataframe that holds all the information
data.to_csv('./data/GMapsAddressesAccurate')

accuracy=round((counter/len(data))*100, 4)
print(accuracy) 
