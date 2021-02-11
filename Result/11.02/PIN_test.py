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
import matplotlib.pyplot as plt


path='c:\\Masha\\Samsung\\1digit\\'
path1='c:\\Masha\\Samsung\\1digit\\clean_1digit\\'

all_i=[]

all_dig=[]
m_i=[]

n=0
for elem in os.listdir(path=path):
    if n>10:
        break
    if "key" in elem:

        my_pin = PIN(elem, path)

        ac_x,ac_y,ac_z=my_pin.fft_pin('acc')

        gyro_x, gyro_y, gyro_z = my_pin.fft_pin('acc')

        m_i.append(my_pin.ret_key()[0])
        if my_pin.ret_key()[0]==9:
            all_i.append(1)
        else:
            all_i.append(0)


        dig = np.concatenate((ac_x,ac_y,ac_z,gyro_x, gyro_y, gyro_z))

        all_dig.append(dig)
        n+=1




all_dig=np.array(all_dig)
all_i=np.array(all_i)
m_i=np.array(m_i)
#dig=np.array(dig)

#print(len(all_dig))
dig_train, dig_test, i_train, i_test = train_test_split(all_dig, all_i, test_size=0.3)
print(i_train)
log_test(dig_train,i_train,dig_test,i_test)
svc_test(dig_train,i_train,dig_test,i_test)
forest_test(dig_train,i_train,dig_test,i_test)


'''dig_train, dig_test, i_train, i_test = train_test_split(all_dig, m_i, test_size=0.5)
#print(all_d)

multi_log_test(dig_train,i_train,dig_test,i_test)
multi_svc_test(dig_train,i_train,dig_test,i_test)
multi_forest_test(dig_train,i_train,dig_test,i_test)'''