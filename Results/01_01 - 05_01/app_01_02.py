import os
import re
import pandas as pd
import scipy.signal as sig
import numpy as np

def filt(file, ax):
    d = pd.read_csv(file)
    col = d[str(ax)]
    y = sig.medfilt(col, kernel_size=3)
    y = sig.savgol_filter(y, window_length=5, polyorder=3,mode='mirror')
    return y, d['timestamp']

        
acc = r'acc_\w+\.csv'
gyro = r'gyro_\w+\.csv'
dirr2 = 'D://samsung//2dig_my'
dirr = 'D://samsung//01_02'
def filtfile(name):
    d = pd.read_csv(name)
    x = d['x']
    new_x = sig.medfilt(x, kernel_size=3)
    new_x = sig.savgol_filter(new_x, window_length=5, polyorder=3,mode='mirror')
    y = d['y']
    new_y = sig.medfilt(y, kernel_size=3)
    new_y = sig.savgol_filter(new_y, window_length=5, polyorder=3,mode='mirror')
    z = d['z']
    new_z = sig.medfilt(z, kernel_size=3)
    new_z = sig.savgol_filter(new_z, window_length=5, polyorder=3,mode='mirror')
    time = d['timestamp']
    ans_x=[]
    ans_y=[]
    ans_z=[]
    ans_t=[]
    n = len(new_x)
    if name[0:3] == 'acc':
        f_name = 'key' + name[3:]
    elif name[0:4] == 'gyro':
        f_name = 'key' + name[4:]
    f = pd.read_csv(f_name)
    t = f.values[1][1]
    print(t)
    for i in range(0,n):
        if t >= time[i]:
            ans_x.append(new_x[i])
            ans_y.append(new_y[i])
            ans_z.append(new_z[i])
            ans_t.append(time[i])
    max_t=max(ans_t)
    min_t=min(ans_t)
    for i in range(0,len(ans_t)):
        ans_t[i] = (ans_t[i]-min_t)/(max_t-min_t)
        ans_x[i] = (ans_x[i] - np.mean(ans_x)) / np.std(ans_x)
        ans_y[i] = (ans_y[i] - np.mean(ans_y)) / np.std(ans_y)
        ans_z[i] = (ans_z[i] - np.mean(ans_z)) / np.std(ans_z)
    l = []
    for i in range(len(ans_x)):
        l.append(str(np.round(ans_x[i],4)) +',' + str(np.round(ans_y[i],4)) +',' + str(np.round(ans_z[i],4))+',' + str(time[i])+'\n')
    f = name[:-4] + 'neww.csv'
    row='x,y,z,timestamp'
    new_f = open(f, 'w')
    new_f.write(row + '\n')
    for i in range(len(ans_x)):
        new_f.write(l[i] + '\n')
    #new_f.close()
    
for root, dirs, files in os.walk(dirr2):
        for name in files:     
            if name[0:3] == 'acc' :
                filtfile(name)
                filtfile('gyro' + name[3:])
                



