import pandas as pd
sumofbirth=0
monthwise=[]
yearlist=[]
l=['Anantapur','Chittoor','East Godavari','Guntur','Krishna','Kurnool','Prakasam','Srikakulam','Nellore','Vishakapatnam','Vizianagaram','West Godavari','Cuddapah']
year=['2017-2018','2018-2019','2019-2020']
for i in year:
    for j in l:
        data=None
        try:
            filename=r'C:\Users\pandu\OneDrive\Desktop\hmdis\xlsxFiles\FlatFile_{}_{}.xlsx'.format(i,j)
            data=pd.read_excel(filename)
        except:
            continue
        datalist=data.values.tolist()
        deathmaternal=0
        deathinfant=0
        birthof=0
        for k in range(4,len(datalist)):
            if(datalist[k][3]=="Total Number of reported live births"):
                birthof=float(datalist[k][5])
            if(datalist[k][3]=="Total no. maternal deaths" or datalist[k][3]=="Total no. maternal deaths"):
                deathmaternal=float(datalist[k][5])
            if(datalist[k][3]=="Total Number of Infant Deaths reported"):
                deathinfant=float(datalist[k][5])
        try:
            mmr=(deathmaternal/birthof)*100000
            imr=(deathinfant/birthof)*1000
        except:
            #print("birth is zero")
            continue
        monthwise=[j,birthof,deathmaternal,mmr]
        yearlist.append(monthwise)
        monthwise=[]

        #print(i,j,mmr,birthof,deathmaternal,sep=' ')
    df=pd.DataFrame(yearlist,columns=['month','live birth','maternal death','mmr'])
    print(df)
    writer=pd.ExcelWriter(r'C:\Users\pandu\OneDrive\Desktop\hmdis\mmr\mmr_{}.xlsx'.format(i))
    df.to_excel(writer)
    writer._save()
    yearlist=[]



    

