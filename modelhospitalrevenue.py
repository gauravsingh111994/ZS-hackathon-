import pandas as pd

from tkinter import filedialog
file=filedialog.askopenfilename(title="Choose HospitalRevenue.csv from you destination")


readhos=pd.read_csv(file)
file=filedialog.askopenfilename(title="Choose HospitalProfile.csv from you destination")
readprofile=pd.read_csv(file)
f=file.split("/")
fout=""
for i in range(0,len(f)-1):
    fout=fout+f[i]+"/"
fout=fout+"modelhospitalrevenue.csv"
for i in range (0,len(readhos)):
    sum=0
    count=0
    
    
    
    did=readhos['District_ID'][i]
    hid=readhos['Hospital_ID'][i]
    emp=readprofile[(readprofile['District_ID']==did) & (readprofile['Hospital_ID']==hid)]['Hospital_employees'].sum()
    if(emp==0):
        emp=1
    for j in range(1,13):
        mon="Month "+str(j)
        
        if(readhos[mon][i]>0):
            sum+=readhos[mon][i]
            count+=1
            
            
    sum=float(sum/emp)
    readhos.loc[i,'Sumperemp']=sum
    readhos.loc[i,'Count']=count
        
        
        
readhos.to_csv(fout,sep=",")
        

