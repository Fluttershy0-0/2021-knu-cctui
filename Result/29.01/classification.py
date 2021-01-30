from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np
from scipy.signal import medfilt


my_d=3
digits = load_digits()
x=[]
m=max(digits.data[1])
All_dig=[]
All_i=np.zeros(100)
for i in range(my_d,500,10):
    x = []
    for j in range(64):
        x.append(digits.data[i][j]/m)
    All_i[int(i/10)] = 1
    All_dig.append(x)
for i in range(500,550):
    x = []
    for j in range(64):
        x.append(digits.data[i][j]/m)
    if digits.target[i]==my_d:
        All_i[i-449] = 1
    All_dig.append(x)



dig_train, dig_test, i_train, i_test = train_test_split(All_dig, All_i, test_size=0.3, random_state=42)



def test(x_train,y_train,x_test,y_test):
    svc = SVC(probability=True)
    tr=svc.fit(x_train, y_train)

    svc_m=confusion_matrix(y_test,tr.predict(x_test))
    svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
    svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR

    svc_pr=tr.predict_proba(x_test)#ефективність моделі
    l2=log_loss(y_test,svc_pr) #log-loss metrics

    svc_f=f1_score(y_test,tr.predict(x_test))#F-score

    print("Опорна векторна машина  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))

print("До шума:")
test(dig_train,i_train,dig_test,i_test)

nois=np.random.normal(0, 0.2, 64)
nois_train=np.zeros((70,64))
nois_test=np.zeros((30,64))

for i in range(len(dig_train)):
    nois_train[i]=dig_train[i]+nois
for i in range(len(dig_test)):
    nois_test[i]=dig_test[i]+nois
#print(dig_train)
#print(dig_test)

new_train=medfilt(nois_train)
new_test=medfilt(nois_test)

print("После очистки от шума:")
test(new_train,i_train,new_test,i_test)