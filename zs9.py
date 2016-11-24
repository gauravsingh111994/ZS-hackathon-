import pandas as pd
from tkinter import filedialog
file=filedialog.askopenfilename(title="Choose HospitalProfiling.csv from you destination")

readprofile=pd.read_csv(file)
file=filedialog.askopenfilename(title="Choose Solution.csv from you destination")

readsol=pd.read_csv(file)
file=filedialog.askopenfilename(title="Choose modelprojectedRevenue.csv")

readpro=pd.read_csv(file)
file=filedialog.askopenfilename(title="Choose modelhospitalRevenue.csv")

readhos=pd.read_csv(file)

f=file.split("/")
fout=""
for i in range(0,len(f)-1):
    fout=fout+f[i]+"/"
fout=fout+"solution.csv"
for i in range(0,len(readsol)):
    
    
    
        
    hid=readsol['Hospital_ID'][i]
    did=readsol['District_ID'][i]
    iid=readsol['Instrument_ID'][i]
    rid=readhos[(readhos['Hospital_ID']==hid) & (readhos['District_ID']==did)]['Region_ID'].unique()
    if(len(rid)==0):
        rid="error"
    else:
        rid=rid[0]
    emp=readprofile[(readprofile['Hospital_ID']==hid) & (readprofile['District_ID']==did)]['Hospital_employees'].sum()
    if(emp==0):
        emp=1
    sumi=readhos[(readhos['Instrument_ID']==iid)]['Sumperemp'].count()
    sumall=readhos['Sumperemp'].count()
    sumi=sumi+readpro[(readpro['Instrument_ID']==iid)]['Sumperemp'].count()
    sumall+=readpro['Sumperemp'].count()
    pis=float(sumi/sumall)
    
    
    
    sumhi=readhos[(readhos['Instrument_ID']==iid) & (readhos['Hospital_ID']==hid)]['Sumperemp'].count()
    sumhiall=readhos[(readhos['Hospital_ID']==hid)]['Sumperemp'].count()
    sumhi+=readpro[(readpro['Instrument_ID']==iid) & (readpro['Hospital_ID']==hid)]['Sumperemp'].count()
    sumhiall+=readpro[(readpro['Hospital_ID']==hid)]['Sumperemp'].count()  
    phis=float(sumhi/sumhiall)
    phos=pis*phis
    
    sumhi=readhos[(readhos['Instrument_ID']==iid) & (readhos['Hospital_ID']!=hid)]['Sumperemp'].count()
    sumhiall=readhos[(readsol['Hospital_ID']==hid)]['Sumperemp'].count()
    sumhi+=readpro[(readpro['Instrument_ID']==iid) & (readpro['Hospital_ID']!=hid)]['Sumperemp'].count()
    sumhiall+=readpro[(readpro['Hospital_ID']==hid)]['Sumperemp'].count()  
    phis=float(sumhi/sumhiall)
    pnhos=pis*phis
    phospital=(phos/(phos+pnhos))
    
    
   
    
    ptotal=(phospital)
  
    if(ptotal>0):
        readsol.loc[i,'Buy_or_not']=1
        
        
        
        sumrev=readhos[(readhos['Instrument_ID']==iid) & (readhos['Hospital_ID']==hid) & (readhos['Region_ID']==rid)]['Sumperemp'].sum()
        sumrevc=readhos[(readhos['Instrument_ID']==iid) & (readhos['Hospital_ID']==hid) & (readhos['Region_ID']==rid)]['Sumperemp'].count()
        if(sumrev==0):
            sumrev=readpro[(readpro['Instrument_ID']==iid) & (readpro['District_ID']==did) ]['Sumperemp'].sum()
            
            sumrevc=readpro[(readpro['Instrument_ID']==iid) & (readpro['District_ID']==did) ]['Sumperemp'].count()

            if(sumrev==0):
                sumrev=0
                sumrevc=1
        readsol.loc[i,'Revenue']=int(float(sumrev/sumrevc)*emp)    
        
            
       
    else:
        readsol.loc[i,'Buy_or_not']=0
        readsol.loc[i,'Revenue']=0
        
        
readsol.to_csv(fout,sep=",")
    
    