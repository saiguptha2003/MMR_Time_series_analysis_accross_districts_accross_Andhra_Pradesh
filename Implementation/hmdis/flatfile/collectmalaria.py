import pandas as pd 
import numpy as np
import os
import glob
import re
l=['Visakhapatnam']
year=['2017-2018','2018-2019','2019-2020']
filename=r"FlatFile_{}_Visakhapatnam.xls".format(year[0])
data = pd.read_html(filename,index_col=1)
dd=data[0].to_csv('ALL.csv')
data=pd.read_csv('ALL.csv')
data.replace(r'^\s*$', np.nan, regex=True)
datalist=data.iloc[2][::2].to_list()
print(datalist)
