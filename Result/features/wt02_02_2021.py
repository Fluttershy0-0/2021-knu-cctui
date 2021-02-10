import os
import numpy as np
from scipy.signal import medfilt,savgol_filter
import csv
import pandas as pd
import pywt
import scipy.fft as fft

#Wavelet Transform
def writef(new_file,x,y,z,t):
    nf= open(new_file, 'w')
    nf.write(row + '\n')
    for i in range(0,len(x)):
        nf.write(str(x[i])+','+str(y[i])+','+str(z[i])+','+str(t[i])+'\n')
p1='c:\\Users\\08041\\Desktop\\for1dig\\fft_and_wt\\'
p2='c:\\Users\\08041\\Desktop\\for1dig\\'
file_list=os.listdir(path=p1)
name=['acc','gyro']
row='x,y,z,timestamp'
os.mkdir("c:\\Users\\08041\\Desktop\\for1dig\\fft_and_wt1\\")
for m in file_list:
    file=p1+m
    
    if name[0] in file or name[1] in file:
        n=p2+'fft_and_wt1\\'+m
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
        fx=pywt.dwt(x[:-1],'db1')
        fy=pywt.dwt(y[:-1],'db1')
        fz=pywt.dwt(z[:-1],'db1')
        writef(n,fx,fy,fz,time)
