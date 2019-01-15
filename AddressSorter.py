import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from gmplot import gmplot

# read in csv as df (with the first column as index_col)
data = pd.read_csv("Jan19_SH.csv", index_col=0)

# remove unwanted columns
unwanted=['opdhVbp', 'vstId', 'vstDate', 'opdhVpulse',
          'opdhVtemp', 'opdhDhtn', 'opdhDihd', 'opdhDhyper']
data.drop(unwanted, inplace=True, axis=1)
# inplace=true tells pd to make the changes in our object
# axis=1 - dropping columns

print('number of rows in df ', len(data))
