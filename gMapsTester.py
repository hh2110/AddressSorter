from functions import *
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import Levenshtein as lev
from gmplot import gmplot
import googlemaps
from datetime import datetime

# this script is checking how good the google maps 
#results are relative to the input 

# read in csv as df (with the first column as index_col)
data = pd.read_csv("./data/GMapsAddress_1329.csv", index_col=0)

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

accuracy=round((counter/len(data))*100, 4)
print('accuracy of the results', accuracy) 

data=data.loc[data['MATCHING']==1]

#save the new dataframe that holds all the information
time=datetime.now().strftime('%H%M')
data.to_csv('./data/GMapsAddressesAccurate_'+time+'.csv')

