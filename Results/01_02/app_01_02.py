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
dirr2 = 'D:/samsung/01_02'
def findfile(drr,mask1,mask2):
    for root, dirs, files in os.walk(drr):
        
        for name in files:
            
            if re.match(mask1, name) or re.match(mask2, name):
                
                x,a = filt(name, 'x')
                y,b = filt(name,'y')
                z,t = filt(name,'z')
                x = list(x)
                
                y = list(y)
                z = list(z)
                t = list(t)
                l = []
                for i in range(len(x)):
                    l.append(str(np.round(x[i],4)) +',' + str(np.round(y[i],4)) +',' + str(np.round(z[i],4))+',' + str(t[i])+'\n')
                f = name[:-4] + 'new.csv'
                row='x,y,z,timestamp'
                new_f = open(f, 'w')
                new_f.write(row + '\n')
                
                for i in range(len(x)):
                    new_f.write(l[i] + '\n')
                    
                 
findfile(dirr2,acc,gyro)    

