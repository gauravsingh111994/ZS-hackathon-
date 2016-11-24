import pandas as pd
from tkinter import filedialog

file=filedialog.askopenfilename(title="Choose ProjectedRevenue.csv from you destination")
readpro=pd.read_csv(file)

file=filedialog.askopenfilename(title="Choose Hospitalprofiling.csv")
readprofile=pd.read_csv(file)
f=file.split("/")
fout=""
for i in range(0,len(f)-1):
    fout=fout+f[i]+"/"
fout=fout+"modelprojectedrevenue.csv"

for i in range(0,len(readpro)):
   
    hid=readpro['Hospital_ID'][i]
    
    did=readpro['District_ID'][i]
    
    emp=readprofile[(readprofile['Hospital_ID']==hid) & (readprofile['District_ID']==did)]['Hospital_employees'].sum()
    if(emp==0):
        emp=1
        
    ar=readpro['Annual_Projected_Revenue'][i]
    readpro.loc[i,'Sumperemp']=float(ar/emp)
    
    
readpro.to_csv(fout,sep=",")