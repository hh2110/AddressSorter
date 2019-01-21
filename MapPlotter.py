import folium
from folium.plugins import HeatMap
import os
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# create dataframe
#data = pd.read_csv('../data/GMapsAddress_1329.csv', index_col=0)
data = pd.read_csv('../data/GMapsAddressesAccurate_1848.csv', index_col=0)
# isloate the lon and lat data
latList=data["LAT"].values;
lonList=data["LON"].values;


# remove any None values for where lon and lat data could not be found
# or where address was not searched for
latList=latList[np.isfinite(latList)];
lonList=lonList[np.isfinite(lonList)];

# use folium to add heat map to map of peshawar 
hmap = folium.Map(location=[33.99, 71.52], zoom_start=12, )

heat = HeatMap( list(zip(latList, lonList)),
                   min_opacity=0.2,
                   max_val=1000,
                   radius=20, blur=15, 
                   max_zoom=10, 
                 )
hmap.add_child(heat)

time=datetime.now().strftime('%H%M')
hmap.save('../data/'+'final_folium'+time+'.html')

