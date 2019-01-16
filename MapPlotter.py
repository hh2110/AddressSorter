import folium
from folium.plugins import HeatMap
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# create dataframe
data = pd.read_csv('./data/GMapsAddressesAccurate.csv', index_col=0)

# isloate the lon and lat data
latList=data["LAT"].values;
lonList=data["LON"].values;

# remove any None values for where lon and lat data could not be found
# or where address was not searched for
latList=latList[latList != np.array(None)]
lonList=lonList[lonList != np.array(None)]

# use folium to add heat map to map of peshawar 
hmap = folium.Map(location=[33.99, 71.52], zoom_start=12, )

heat = HeatMap( list(zip(data.LAT.values, data.LON.values)),
                   min_opacity=0.2,
                   max_val=100,
                   radius=20, blur=15, 
                   max_zoom=10, 
                 )

hmap.add_child(heat)
hmap.save(os.path.join('data', 'folium.html'))

