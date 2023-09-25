import pandas as pd
import xlwt
filef=pd.read_excel(r"C:\Users\pandu\OneDrive\Desktop\hmdis\f2_files\A-Andhra Pradesh_Apr.xlsx",index_col=1)
l=set()
for i in range(len(filef)):
    l.add(filef.iloc[i][1])
for i in l:
    open("district.txt","a").write(str(i)+"\n")

