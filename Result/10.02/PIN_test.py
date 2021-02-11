from PINclass import PIN
from sklearn.model_selection import train_test_split
from binar_test import log_test,svc_test,forest_test
from multi_test import multi_svc_test,multi_log_test,multi_forest_test
import os
import numpy as np
import scipy.fftpack
import pywt
import pandas as pd
import scipy.fftpack

path='c:\\Masha\\Samsung\\1digit\\'
path1='c:\\Masha\\Samsung\\1digit\\clean_1digit\\'
path2='c:\\Masha\\Samsung\\Task0802\\makowetska\\'
path3='c:\\Masha\\Samsung\\Task0802\\novikova\\'
all_i=[]
all_dig=[]
dig=[]
m_i=[]

#print('key_06yAihAZkFoMZPUk7vqF.csv' in os.listdir(path))
for elem in os.listdir(path=path):
    if "key" in elem:
        #print(elem)
        my_pin = PIN(elem, path)
        my_pin.sigm_time('acc')
        my_pin.sigm_time('gyro')

        a_f = pd.read_csv(path1 + 'new_acc' + elem[3:len(elem)])
        ac_x = a_f['x'].values
        ac_y = a_f['y'].values
        ac_z = a_f['z'].values

        #ac_x = np.abs(scipy.fftpack.fft(ac_x))
        #ac_y = np.abs(scipy.fftpack.fft(ac_y))
        #ac_z = np.abs(scipy.fftpack.fft(ac_z))
        #print(scipy.fftpack.fft(ac_x))
        n1=len(ac_x)

        f = pd.read_csv(path1 + 'new_gyro' + elem[3:len(elem)])
        gyro_x = f['x'].values
        gyro_y = f['y'].values
        gyro_z = f['z'].values

        #gyro_x = np.abs(scipy.fftpack.fft(gyro_x))
        #gyro_y = np.abs(scipy.fftpack.fft(gyro_y))
        #gyro_z = np.abs(scipy.fftpack.fft(gyro_z))
        n2=len(gyro_x)


        m_i.append(my_pin.ret_key()[0])
        if my_pin.ret_key()[0]==3:
            all_i.append(1)
        else:
            all_i.append(0)
        #all_dig.append([ac_z[n1 - 1], gyro_y[n2 - 1]])
        all_dig.append([ac_x[n1-1],ac_y[n1-1],ac_z[n1-1],gyro_x[n2-1],gyro_y[n2-1],gyro_z[n2-1]])
        dig.append([gyro_y[n2-1]])




'''for elem in os.listdir(path=path2):
    if "key" in elem:
        my_pin = PIN(elem, path2)
        #all_i.append(0)
        m_i.append([my_pin.ret_key()[0]])
        a_f = pd.read_csv(path2 + 'acc' + elem[3:len(elem)])
        ac_x = a_f['x'].values
        ac_y = a_f['y'].values
        ac_z = a_f['z'].values
        n = len(ac_x) - 1
        f = pd.read_csv(path2 + 'gyro' + elem[3:len(elem)])
        gyro_x = f['x'].values
        gyro_y = f['y'].values
        gyro_z = f['z'].values

        n1 = len(gyro_x) - 1

        all_dig.append([ac_x[n], ac_y[n], ac_z[n], gyro_x[n1], gyro_y[n1], gyro_z[n1]])
        '''

for elem in os.listdir(path3):
    if "key" in elem:
        my_pin = PIN(elem, path3)
        #my_pin.sigm_time('acc')
        #my_pin.sigm_time('gyro')

        a_f = pd.read_csv(path3 + 'acc' + elem[3:len(elem)])
        ac_x = a_f['x'].values
        ac_y = a_f['y'].values
        ac_z = a_f['z'].values

        #ac_x = np.abs(scipy.fftpack.fft(ac_x))
        #ac_y = np.abs(scipy.fftpack.fft(ac_y))
        #ac_z = np.abs(scipy.fftpack.fft(ac_z))
        n1=len(ac_x)

        f = pd.read_csv(path3 + 'gyro' + elem[3:len(elem)])
        gyro_x = f['x'].values
        gyro_y = f['y'].values
        gyro_z = f['z'].values

        #gyro_x = np.abs(scipy.fftpack.fft(gyro_x))
        #gyro_y = np.abs(scipy.fftpack.fft(gyro_y))
        #gyro_z = np.abs(scipy.fftpack.fft(gyro_z))

        n2=len(gyro_x)

        m_i.append(my_pin.ret_key()[0])
        if my_pin.ret_key()[0] == 3:
            all_i.append(1)
        else:
            all_i.append(0)
        #all_dig.append([ac_z[n1 - 1], gyro_y[n2 - 1]])
        all_dig.append([ac_x[n1 - 1], ac_y[n1 - 1], ac_z[n1 - 1], gyro_x[n2 - 1], gyro_y[n2 - 1], gyro_z[n2 - 1]])
        dig.append([gyro_y[n2-1]])

all_dig=np.array(all_dig)
all_i=np.array(all_i)
m_i=np.array(m_i)
dig=np.array(dig)

#print(len(all_dig))
'''dig_train, dig_test, i_train, i_test = train_test_split(all_dig, all_i, test_size=0.3)
log_test(dig_train,i_train,dig_test,i_test)
svc_test(dig_train,i_train,dig_test,i_test)
forest_test(dig_train,i_train,dig_test,i_test)'''




dig_train, dig_test, i_train, i_test = train_test_split(dig, m_i, test_size=0.3)


multi_log_test(dig_train,i_train,dig_test,i_test)
multi_svc_test(dig_train,i_train,dig_test,i_test)
multi_forest_test(dig_train,i_train,dig_test,i_test)