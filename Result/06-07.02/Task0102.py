import os
import numpy as np
from scipy.signal import medfilt,savgol_filter
import csv
import matplotlib.pyplot as plt
import pandas as pd

#Done:
# Segmentation of preprocessed signals into parts for each element of PIN
#Time normalization for obtained segments
#noise suppression with median and Savitzky-Golay filters
#Amplitude normalization of prepared data with standard scaler



path='c:\\Masha\\Samsung\\1digit\\'
path1='c:\\Masha\\Samsung\\'
file_list=os.listdir(path=path)
name=['acc','gyro','key']
row='x,y,z,timestamp'
gyro=[]
key=[]
n=0
if ('clean_1digit' in os.listdir(path1))==False:
    os.mkdir("c:\\Masha\\Samsung\\clean_1digit\\")

def file_read(file_name):
    f = open(file_name, newline='')
    reader = csv.reader(f)
    x=[]
    y=[]
    z=[]
    t=[]
    a=0
    for row in reader:
        if a>0:
            x.append(float(row[0]))
            y.append(float(row[1]))
            z.append(float(row[2]))
            t.append(int(row[3]))
        a+=1
    return x,y,z,t

def write_file(file_name,x,y,z,t):
    new_f = open(file_name, 'w')
    new_f.write(row + '\n')
    for i in range(0,len(x)):
        new_f.write(str(round(x[i],5))+','+str(round(y[i],5))+','+str(round(z[i],5))+','+str(t[i])+'\n')

def sigm_time(path,name_a,pin_name):
    f = pd.read_csv(path+pin_name)
    t = f.values[0][1]
    name=pin_name[3:len(pin_name)]
    name1=name_a+name
    f1 = pd.read_csv("c:\\Masha\\Samsung\\clean_1digit\\"+"clean_"+name1)
    x=f1['x'].values
    y=f1['y'].values
    z=f1['z'].values
    time=f1['timestamp'].values
    res_x=[]
    res_y=[]
    res_z=[]
    res_t=[]
    n=len(x)

    for i in range(0,n):
        if t>=time[i]:
            res_x.append(x[i])
            res_y.append(y[i])
            res_z.append(z[i])
            res_t.append(time[i])
    max_t=max(res_t)
    min_t=min(res_t)

    for i in range(0,len(res_t)):
        res_t[i]=(res_t[i]-min_t)/(max_t-min_t)
        res_x[i]=(res_x[i]-np.mean(res_x))/np.std(res_x)
        res_y[i] = (res_y[i] - np.mean(res_y)) / np.std(res_y)
        res_z[i] = (res_z[i] - np.mean(res_z)) / np.std(res_z)

    return res_x,res_y,res_z,res_t


for elem in file_list:
    file_name=path+elem

    '''if name[0] in file_name or name[1] in file_name:
        new_name=path1+'clean_1digit\\'+"clean"+"_"+elem
        new_f=open(new_name,'w')
        x,y,z,time=np.array(file_read(file_name))
        new_x = medfilt(x, 3)
        res_x = savgol_filter(new_x, 7, 1)
        new_y = medfilt(y, 3)
        res_y = savgol_filter(new_y, 7, 1)
        new_z = medfilt(z, 3)
        res_z = savgol_filter(new_z, 7, 1)
        write_file(new_name,res_x,res_y,res_z,time)'''

    if name[2] in file_name:
        print("Accelerometr: ",sigm_time(path,name[0],elem))
        print("Gyroscop: ",sigm_time(path,name[1], elem))

