import pandas as pd
import xlwt
import bs4 as bs
import time
import numpy as np
import pyexcel as p
l=['Anantapur','Chittoor','East Godavari','Guntur','Krishna','Kurnool','Prakasam','Srikakulam','Nellore','Vishakapatnam','Vizianagaram','West Godavari','Cuddapah']
year=['2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020']
for i in year:
    for j in l:
        data=pd.read_excel(r"C:\Users\pandu\OneDrive\Desktop\hmdis\flatfile\FlatFile_{}_{}.xls".format(i,j))
        print(data[0])


