import os
import csv
import numpy as np
import pandas as pd

path = "C:\\work\\2021-knu-cctui\\Data"
file_list = os.listdir(path=path)
name = ['acc','gyro','key']
row = 'x,y,z,timestamp'
gyro = []
key = []
n = 0


def file_read(file_name):
    f = open(file_name, newline='')
    reader = csv.reader(f)
    x = []
    y = []
    z = []
    time_st = []
    a = 0
    for row in reader:
        if a>0:
            x.append(float(row[0]))
            y.append(float(row[1]))
            z.append(float(row[2]))
            time_st.append(int(row[3]))
        a += 1
    return x,y,z,time_st

def write_file(file_name,x,y,z,time_st):
    new_f = open(file_name, 'w')
    new_f.write(row + '\n')
    for i in range(0,len(x)):
        new_f.write(str(round(x[i],5))+','+str(round(y[i],5))+','+str(round(z[i],5))+','+str(time_st[i])+'\n')

def sigm_time(path,name_dataset,pin_name):
    datset = pd.read_csv(path+pin_name)
    t = datset.values[0][1]
    name = pin_name[3:len(pin_name)]
    name1 = name_dataset+name
    data = pd.read_csv("C:\\work\\2021-knu-cctui\\Data"+"clean_"+name1)
    x, y, z, time = data['x'].values, data['y'].values, data['z'].values,  data['timestamp'].values
    res_x = []
    res_y = []
    res_z = []
    res_time = []
    n = len(x)

    for i in range(0,n):
        if t >= time[i]:
            res_x.append(x[i])
            res_y.append(y[i])
            res_z.append(z[i])
            res_time.append(time[i])
    max_t, min_t = max(res_time), min(res_time)

    for i in range(0,len(res_time)):
        res_x[i]=(res_x[i]-np.mean(res_x))/np.std(res_x)
        res_y[i] = (res_y[i] - np.mean(res_y)) / np.std(res_y)
        res_z[i] = (res_z[i] - np.mean(res_z)) / np.std(res_z)
        res_time[i] = (res_time[i]-min_t)/(max_t-min_t)

    return res_x, res_y, res_z, res_time


for elem in file_list:
    file_name = path+elem

    if name[2] in file_name:
        print("Accelerometr: ",sigm_time(path,name[0],elem))
        print("Gyroscop: ",sigm_time(path,name[1], elem))