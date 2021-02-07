import os
import numpy as np
from scipy.signal import medfilt,savgol_filter
import csv
def readf(file):
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
        a=a+1
    return x,y,z,t
def writef(file,x,y,z,t):
    new_f = open(file, 'w')
    new_f.write(row + '\n')
    for i in range(0,len(x)):
        new_f.write(str(round(x[i],5))+','+str(round(y[i],5))+','+str(round(z[i],5))+','+str(t[i])+'\n')
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
        x,y,z,time=np.array(readf(file))
        medf_x = medfilt(x, 3)
        medf_y = medfilt(y, 3)
        medf_z = medfilt(z, 3)
        sf_x = savgol_filter(medf_x, 5, 1)
        sf_y = savgol_filter(medf_y, 5, 1)
        sf_z = savgol_filter(medf_z, 5, 1)
        writef(n,sf_x,sf_y,sf_z,time)

