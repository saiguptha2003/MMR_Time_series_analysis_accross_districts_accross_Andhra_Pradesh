import xlrd
import numpy as np
import pyexcel as p
import pandas as pd 

import pandas
import openpyxl
year=['2020-2021','2021-2022','2022-2023']
month=['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M']
import csv
datamain=[]
for i in year:
    fields=['module','items','urban','rural']
    print(i)
    for j,k in zip(alpha,month):
        filer=r'C:\Users\pandu\OneDrive\Desktop\hmdis\f2_files\files\{}_{}_{}.xlsx'.format(j,k,i)
        print(filer)
        dataframe=pd.read_excel(filer)
        datamain=[]
        for r in range(7,len(dataframe)):
            datali=[]
            datalist=dataframe.iloc[r][0:].to_list()
            datali.append(datalist[0])
            datali.append(datalist[2])
            datali.append(datalist[4])
            datali.append(datalist[5])
            datamain.append(datali)
        filename="f2_files/flatfiles/{}_{}.csv".format(k,i)
        with open(filename,'a') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(datamain)


print(datamain)
