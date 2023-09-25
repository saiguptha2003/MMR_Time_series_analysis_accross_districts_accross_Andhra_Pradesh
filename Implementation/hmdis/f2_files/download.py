import requests
import os
l=['Anantapur','Chittoor','East Godavari','Guntur','Krishna','Kurnool','Prakasam','Srikakulam','Nellore','Visakhapatnam','Vizianagaram','West Godavari','Cuddapah']
link="https://hmis.mohfw.gov.in/downloadfiles?filepath=/Standard%20Reports/5~C2.%20Data%20Itemwise%20Monthly%20(up%20to%20sub%20district)/2.%20All%20States%20Across%20Districts/2020-2021(Data%20is%20Provisional)/B.Cummulative/Andhra%20Pradesh/A-Andhra%20Pradesh_UpTo_Apr.xlsx"
errorlist=[]
year=['2020-2021','2021-2022','2022-2023','2023-2024','2009-2010','2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020']
month=['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar']
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M']
ziplink='https://hmis.mohfw.gov.in/downloadfiles?filepath=/Standard%20Reports/5~C2.%20Data%20Itemwise%20Monthly%20(up%20to%20sub%20district)/2.%20All%20States%20Across%20Districts/2008-2009.zip'
print(len(l))
def download_file(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    else:
        print('Error downloading file: {}'.format(response.status_code))
        errorlist.append(filename)
print(errorlist)
if __name__ == '__main__':
    for k in year:
        for i,j in zip(alpha,month):
            url = 'https://hmis.mohfw.gov.in/downloadfiles?filepath=/Standard%20Reports/5~C2.%20Data%20Itemwise%20Monthly%20(up%20to%20sub%20district)/2.%20All%20States%20Across%20Districts/{}(Data%20is%20Provisional)/B.Cummulative/Andhra%20Pradesh/{}-Andhra%20Pradesh_UpTo_{}.xlsx'.format(k,i,j)
            print(url)
            filename = r'C:\Users\pandu\OneDrive\Desktop\hmdis\f2_files\files\{}_{}_{}.xlsx'.format(i,j,k)
            download_file(url, filename)
            print('File downloaded successfully!')

