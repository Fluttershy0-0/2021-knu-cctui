import pandas as pd
import numpy as np

def segm(f_name,clean_name):
    f = pd.read(f_name)
    t = f.values[0][1]
    f1 = pd.read_csv(clean_name)
    x=f1['x'].values
    y=f1['y'].values
    z=f1['z'].values
    time=f1['timestamp'].values
    ans_x=[]
    ans_y=[]
    ans_z=[]
    ans_t=[]
    n=len(x)

    for i in range(0,n):
        if t>=time[i]:
            ans_x.append(x[i])
            ans_y.append(y[i])
            ans_z.append(z[i])
            ans_t.append(time[i])
    max_t=max(ans_t)
    min_t=min(ans_t)

    for i in range(0,len(ans_t)):
        ans_t[i]=(ans_t[i]-min_t)/(max_t-min_t)
        ans_x[i]=(ans_x[i]-np.mean(ans_x))/np.std(ans_x)
        ans_y[i] = (ans_y[i] - np.mean(ans_y)) / np.std(ans_y)
        ans_z[i] = (ans_z[i] - np.mean(ans_z)) / np.std(ans_z)

    return ans_x,ans_y,ans_z,ans_t


