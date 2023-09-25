import xlrd
import pandas as pd
import csv
l=['Anantapur','Chittoor','East Godavari','Guntur','Krishna','Kurnool','Prakasam','Srikakulam','Nellore','Vishakapatnam','Vizianagaram','West Godavari','Cuddapah']
year=['2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020']
def csv_from_excel(filename,i,j):
    wb = xlrd.open_workbook(filename)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(r'C:\Users\pandu\OneDrive\Desktop\hmdis\xlsxFiles\csvfiles\FlatFile_{}_{}.csv'.format(i,j), 'w')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


# Reading an excel file


# Converting excel file into CSV file
for i in year:
    for j in l:
        filename=r"C:\Users\pandu\OneDrive\Desktop\hmdis\xlsxFiles\FlatFile_{}_{}.xlsx".format(i,j)
        excelFile=None
        try:
            excelFile = pd.read_excel (filename)
        except:
            continue
        excelFile.to_csv (r"C:\Users\pandu\OneDrive\Desktop\hmdis\xlsxFiles\csvfiles\FlatFile_{}_{}.csv".format(i,j), index = i, header=True)

