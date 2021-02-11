import os
import numpy as np
from scipy.signal import medfilt,savgol_filter
import csv
import pandas as pd
import scipy.fft as fft
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.multiclass import OneVsRestClassifier
class PIN:
    def __init__(self,name_zero,path):
        self.file=name_zero
        self.path=path
        if ('filt' in os.listdir(path)) == False:
            os.mkdir(path+"filt\\")
        self.newpath=path+"filt\\"
    def readf(self,name0):
        name = self.file[3:len(self.file)]
        name_first = self.path + name0 + name
        f = open(name_first, newline='')
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
        f.close()
        return x, y, z, t

    def denois(self,name0):
        name = self.file[3:len(self.file)]
        name_first = self.path+name0 + name
        x, y, z, time = np.array(self.readf(name0))
        medf_x = medfilt(x, 3)
        medf_y = medfilt(y, 3)
        medf_z = medfilt(z, 3)
        sf_x = savgol_filter(medf_x, 5, 1)
        sf_y = savgol_filter(medf_y, 5, 1)
        sf_z = savgol_filter(medf_z, 5, 1)
        return sf_x,sf_y,sf_z,time
    



    def sigm_norm(self,name0):
        k1= pd.read_csv(self.path + self.file)
        k= k1.values[0][1]
        name=self.file[3:len(self.file)]
        name_first=name0+name
        x,y,z,time=self.denois(name0)
        sig_x = []
        sig_y = []
        sig_z = []
        sig_t = []
        n = len(x)

        for i in range(0, n):
            if k>= time[i]:
                sig_x.append(x[i])
                sig_y.append(y[i])
                sig_z.append(z[i])
                sig_t.append(time[i])
        max_t = max(sig_t)
        min_t = min(sig_t)

        for i in range(0, len(sig_t)):
            sig_t[i] = (sig_t[i] - min_t) / (max_t - min_t)
            sig_x[i] = (sig_x[i] - np.mean(sig_x)) / np.std(sig_x)
            sig_y[i] = (sig_y[i] - np.mean(sig_y)) / np.std(sig_y)
            sig_z[i] = (sig_z[i] - np.mean(sig_z)) / np.std(sig_z)

        new_name = self.newpath + "sigm_" +name_first
        row = 'x,y,z,timestamp'
        nf = open(new_name, 'w')
        nf.write(row+'\n')

        for i in range(0, len(sig_x)):
            nf.write(str(round(sig_x[i], 4)) + ',' + str(round(sig_y[i], 4)) + ',' + str(round(sig_z[i], 4)) + ',' + str(round(sig_t[i],4)) + '\n')

        return sig_x, sig_y, sig_z, sig_t
    def keys(self):
        f = pd.read_csv(self.path+self.file)
        t = int(f.values[0][1])
        key=int(f.values[0][0])

        return key,t

    

    def FFT(self,name0):
        x = np.abs(fft.fft(sigm_norm(name0)[0]))
        y = np.abs(fft.fft(sigm_norm(name0)[1]))
        z = np.abs(fft.fft(sigm_norm(name0)[2]))
        return x,y,z
def mul_l_reg(x_train,y_train,x_test,y_test):
    log = OneVsRestClassifier(LogisticRegression())
    m= log.fit(x_train, y_train)
    predic= m.predict_proba(x_test) 
    log_l=log_loss(y_test, predic)  
    f1 = f1_score(y_test, m.predict(x_test),average = 'weighted') 
    print('log-loss = ', log_l,'F-score = ', f1)
def mul_supVecMa(x_train ,y_train ,x_test ,y_test):
    svc = OneVsRestClassifier(SVC(probability=True))
    m= svc.fit(x_train, y_train)
     
    predic= m.predict_proba(x_test) 
    log_l= log_loss(y_test ,predic) 
    f1 = f1_score(y_test ,m.predict(x_test),average = 'weighted')  
    print('log-loss = ', log_l,'F-score = ', f1)
def mul_forest(x_train,y_train,x_test,y_test):
    tree = OneVsRestClassifier(DecisionTreeClassifier())
    m= tree.fit(x_train, y_train)
    predic= m.predict_proba(x_test)
    log_l= log_loss(y_test,predic) 
    f1= f1_score(y_test,m.predict(x_test),average = 'weighted')

    print('log-loss = ', log_l,'F-score = ', f1)

p='c:\\Users\\08041\\Desktop\\for1dig\\1digproj\\'
p1='c:\\Users\\08041\\Desktop\\for1dig\\filt\\'
p2='c:\\Users\\08041\\Desktop\\for1dig\\1digprojtest\\'
w=[]
dig_zero=[]
dig_first=[]
v=[]

for elem in os.listdir(path=p):
    if 'key' in elem:
        odp=PIN(elem,p)
        odp.sigm_norm('acc')
        odp.sigm_norm('gyro')
        f1=pd.read_csv(p1+'acc'+elem[3:len(elem)])
        accx=f1['x'].values
        accy=f1['y'].values
        accz=f1['z'].values
        accx=np.abs(fft.fft(accx))
        accy=np.abs(fft.fft(accy))
        accz=np.abs(fft.fft(accz))
        n_first=len(accx)
        f2=pd.read_csv(p1+'gyro'+elem[3:len(elem)])
        gyrox=f2['x'].values
        gyroy=f2['y'].values
        gyroz=f2['z'].values
        gyrox=np.abs(fft.fft(gyrox))
        gyroy=np.abs(fft.fft(gyroy))
        gyroz=np.abs(fft.fft(gyroz))
        n_second=len(gyrox)
        v.append(odp.keys()[0])
        if odp.keys()[0]==3:
            w.append(1)
        else:
            w.append(0)
        dig_zero.append([accx[n_first-1],accy[n_first-1],accz[n_first-1],gyrox[n_second-1],gyroy[n_second-1],gyroz[n_second-1]])
        dig_first.append([gyroy[n_second-1]])
for elem in os.listdir(p2):
    if 'key' in elem:
        odp=PIN(elem, p2)
        odp.sigm_norm('acc')
        odp.sigm_norm('gyro')
        f1=pd.read_csv(p2+'acc'+elem[3:len(elem)])
        accx=f1['x'].values
        accy=f1['y'].values
        accz=f1['z'].values
        accx=np.abs(fft.fft(accx))
        accy=np.abs(fft.fft(accy))
        accz=np.abs(fft.fft(accz))
        n_first=len(accx)
        f2=pd.read_csv(p2+'gyro'+elem[3:len(elem)])
        gyrox=f2['x'].values
        gyroy=f2['y'].values
        gyroz=f2['z'].values
        gyrox=np.abs(fft.fft(gyrox))
        gyroy=np.abs(fft.fft(gyroy))
        gyroz=np.abs(fft.fft(gyroz))
        n_second=len(gyrox)
        v.append(odp.keys()[0])
        if odp.keys()[0]==3:
            w.append(1)
        else:
            w.append(0)
        dig_zero.append([accx[n_first-1],accy[n_first-1],accz[n_first-1],gyrox[n_second-1],gyroy[n_second-1],gyroz[n_second-1]])
        dig_first.append([gyroy[n_second-1]])
dig_zero=np.array(dig_zero)
w=np.array(w)
v=np.array(v)
dig_first=np.array(dig_first)

x_train, x_test, y_train, y_test=train_test_split(dig_first,v, test_size=0.3)
mul_l_reg(x_train, y_train, x_test, y_test)
mul_supVecMa(x_train, y_train, x_test, y_test)
mul_forest(x_train, y_train, x_test, y_test)
