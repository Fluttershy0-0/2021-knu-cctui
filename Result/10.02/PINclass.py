import os
import numpy as np
from scipy.signal import medfilt,savgol_filter
import csv
import pandas as pd
import scipy.fftpack


class PIN:
    def __init__(self,file_name,path):
        self.file=file_name
        self.path=path
        if ('clean_1digit' in os.listdir(path)) == False:
            os.mkdir(path+"clean_1digit\\")
        self.newpath=path+"clean_1digit\\"
    def file_read(self,name_a):
        name = self.file[3:len(self.file)]
        name1 = self.path + name_a + name
        f = open(name1, newline='')
        reader = csv.reader(f)
        x = []
        y = []
        z = []
        t = []
        a = 0
        for row in reader:
            if a > 0:
                x.append(float(row[0]))
                y.append(float(row[1]))
                z.append(float(row[2]))
                t.append(int(row[3]))
            a += 1
        f.close()
        return x, y, z, t

    def clean_nois(self,name_a):
        name = self.file[3:len(self.file)]
        name1 = self.path+name_a + name
        x, y, z, time = np.array(self.file_read(name_a))
        new_x = medfilt(x, 3)
        res_x = savgol_filter(new_x, 7, 2)
        new_y = medfilt(y, 3)
        res_y = savgol_filter(new_y, 7, 2)
        new_z = medfilt(z, 3)
        res_z = savgol_filter(new_z, 7, 2)
        return res_x,res_y,res_z,time



    def sigm_time(self,name_a):
        f = pd.read_csv(self.path + self.file)
        t = f.values[0][1]
        name = self.file[3:len(self.file)]
        name1 = name_a + name
        x,y,z,time=self.clean_nois(name_a)
        res_x = []
        res_y = []
        res_z = []
        res_t = []
        n = len(x)

        for i in range(0, n):
            if t >= time[i]:
                res_x.append(x[i])
                res_y.append(y[i])
                res_z.append(z[i])
                res_t.append(time[i])
        max_t = max(res_t)
        min_t = min(res_t)

        for i in range(0, len(res_t)):
            res_t[i] = (res_t[i] - min_t) / (max_t - min_t)
            res_x[i] = (res_x[i] - np.mean(res_x)) / np.std(res_x)
            res_y[i] = (res_y[i] - np.mean(res_y)) / np.std(res_y)
            res_z[i] = (res_z[i] - np.mean(res_z)) / np.std(res_z)

        new_name = self.newpath + "new_" +name1
        row = 'x,y,z,timestamp'
        new_f = open(new_name, 'w')
        new_f.write(row+'\n')

        for i in range(0, len(res_x)):
            new_f.write(str(round(res_x[i], 5)) + ',' + str(round(res_y[i], 5)) + ',' + str(round(res_z[i], 5)) + ',' + str(round(res_t[i],5)) + '\n')

        return res_x, res_y, res_z, res_t

    def ret_key(self):
        f = pd.read_csv(self.path+self.file)
        t = int(f.values[0][1])
        key=int(f.values[0][0])

        return key,t

    def fft_pin(self,name_a):
        x = np.abs(scipy.fftpack.fft(sigm_time(name_a)[0]))
        y = np.abs(scipy.fftpack.fft(my_pin.sigm_time(name_a)[1]))
        z = np.abs(scipy.fftpack.fft(my_pin.sigm_time(name_a)[2]))
        return x,y,z

