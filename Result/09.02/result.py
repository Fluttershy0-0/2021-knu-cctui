from PINclass import PIN
from sklearn.model_selection import train_test_split
from binar_test import log_test,svc_test,forest_test
from multi_test import multi_svc_test,multi_log_test,multi_forest_test
import os
import numpy as np



path='c:\\Masha\\Samsung\\1digit\\'
path2='c:\\Masha\\Samsung\\Task0802\\makowetska\\'
path3='c:\\Masha\\Samsung\\Task0802\\novikova\\'
all_i=[]
all_dig=[]

m_i=[]
for elem in os.listdir(path=path):
    if "key" in elem:
        my_pin = PIN(elem, path)
        my_pin.sigm_time('acc')
        my_pin.sigm_time('gyro')
        all_i.append(1)
        m_i.append(1)
        all_dig.append([my_pin.ret_key()[1]])

for elem in os.listdir(path=path2):
    if "key" in elem:
        my_pin = PIN(elem, path2)
        all_i.append(0)
        m_i.append(0)
        all_dig.append([my_pin.ret_key()[1]])

for elem in os.listdir(path=path3):
    if "key" in elem:
        my_pin = PIN(elem, path3)
        all_i.append(0)
        m_i.append(2)
        all_dig.append([my_pin.ret_key()[1]])
all_dig=np.array(all_dig)
all_i=np.array(all_i)
m_i=np.array(m_i)

dig_train, dig_test, i_train, i_test = train_test_split(all_dig, all_i, test_size=0.3, random_state=42)
log_test(dig_train,i_train,dig_test,i_test)
svc_test(dig_train,i_train,dig_test,i_test)
forest_test(dig_train,i_train,dig_test,i_test)


dig_train, dig_test, i_train, i_test = train_test_split(all_dig, m_i, test_size=0.3)
multi_log_test(dig_train,i_train,dig_test,i_test)
multi_svc_test(dig_train,i_train,dig_test,i_test)
multi_forest_test(dig_train,i_train,dig_test,i_test)