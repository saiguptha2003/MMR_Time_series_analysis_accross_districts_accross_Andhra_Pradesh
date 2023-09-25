import pandas as pd
import xlwt
from xlwt import Workbook
import bs4 as bs
import time
import xlrd
import numpy as np
import pyexcel as p
import openpyxl
year=['2020-2021','2021-2022','2022-2023','2023-2024']
month=['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M']
import csv
datamain=[]
for i in year:
    print(i)
    for j,k in zip(alpha,month):
        filer=r'C:\Users\pandu\OneDrive\Desktop\hmdis\f2_files\files\{}_{}_{}.xlsx'.format(j,k,i)
        print(filer)
        dataframe=pd.read_excel(filer)
        for i in range(7,len(dataframe)):
            datali=[]
            datalist=dataframe.iloc[i][0:].to_list()
            datali.append(datalist[0])
            datali.append(datalist[1])
            datali.append(datalist[3])
            datali.append(datalist[4])
            datamain.append(datali)

print(datamain)

    




