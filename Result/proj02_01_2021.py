import os
import numpy as np
from scipy.signal import medfilt,savgol_filter
import csv
import pandas as pd
#medfilt, savgol_filter, sigmentation, norm
def writef(new_file,x,y,z,t):
    nf= open(new_file, 'w')
    nf.write(row + '\n')
    for i in range(0,len(x)):
        nf.write(str(round(x[i],5))+','+str(round(y[i],5))+','+str(round(z[i],5))+','+str(t[i])+'\n')
def sigm_norm(p,elem,q):
    k1=pd.read_csv(p+elem)
    
    k=k1.values[0][1]
    
    u=elem[3:len(elem)]
    b=q+u
    g=pd.read_csv("c:\\Users\\08041\\Desktop\\for1dig\\filt\\"+b)
    
    x=g['x']
    y=g['y']
    z=g['z']
    time=g['timestamp']
    fx=[]
    fy=[]
    fz=[]
    ft=[]
    for i in range(0, len(x)):
        if k>=time[i]:
            fx.append(x[i])
            fy.append(y[i])
            fz.append(z[i])
            ft.append(time[i])
    maxt=max(ft)
    mint=min(ft)
    for i in range(0, len(ft)):
        ft[i]=(ft[i]-mint)/(maxt-mint)
        fx[i]=(fx[i]-np.mean(fx))/np.std(fx)
        fy[i]=(fy[i]-np.mean(fy))/np.std(fy)
        fz[i]=(fz[i]-np.mean(fz))/np.std(fz)
    
    
    return ft,fx,fy,fz
   
    
p1='c:\\Users\\08041\\Desktop\\for1dig\\1digproj\\'
p2='c:\\Users\\08041\\Desktop\\for1dig\\'
file_list=os.listdir(path=p1)
name=['acc','gyro','key']
row='x,y,z,timestamp'
os.mkdir("c:\\Users\\08041\\Desktop\\for1dig\\filt\\")
for m in file_list:
    file=p1+m
    
    if name[0] in file or name[1] in file:
        n=p2+'filt\\'+m
        f0=open(n,'w')
        f=open(file, newline='')
        r=csv.reader(f)
        x=[]
        y=[]
        z=[]
        t=[]
        a=0
        for row in r:
            if a>0:
                x.append(float(row[0]))
                y.append(float(row[1]))
                z.append(float(row[2]))
                t.append(int(row[3]))
            a+=1
        
        row='x,y,z,timestamp'
        x=np.array(x)
        y=np.array(y)
        z=np.array(z)
        time=np.array(t)
        medf_x = medfilt(x, 3)
        medf_y = medfilt(y, 3)
        medf_z = medfilt(z, 3)
        sf_x = savgol_filter(medf_x, 7, 1)
        sf_y = savgol_filter(medf_y, 7, 1)
        sf_z = savgol_filter(medf_z, 7, 1)
        writef(n,sf_x,sf_y,sf_z,time)
    #if name[2] in file:
        #sigm_norm(p1,m,name[0])
        #sigm_norm(p1,m,name[1])
