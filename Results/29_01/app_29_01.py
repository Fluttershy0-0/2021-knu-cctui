import numpy as np
from sklearn.svm import SVC

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from scipy.signal import medfilt
dig = 4
digits = datasets.load_digits()
m = max(digits.data[1])
_ = i=np.zeros(100)
data = []
for i in range(dig,500,10):
    x = []
    for j in range(64):
        x.append(digits.data[i][j]/m)
    _[int(i/10)] = 1
    data.append(x)
for i in range(500,550):
    x = []
    for j in range(64):
        x.append(digits.data[i][j]/m)
    if digits.target[i]==dig:
        _[i-449] = 1
    data.append(x)

x_train, x_test, y_train, y_test = train_test_split(
    data, _, test_size=0.3,train_size=0.7,random_state=10, shuffle=True)

svc = SVC(probability=True)
tr = svc.fit(x_train, y_train)

svc_m = confusion_matrix(y_test,tr.predict(x_test))
svc_far = svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])
svc_frr = svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])

svc_pr = tr.predict_proba(x_test)
l = log_loss(y_test,svc_pr) 

svc_f=f1_score(y_test,tr.predict(x_test))
print("before noise: ")
print("FAR =", svc_far, "\nFRR = ",svc_frr,"\nlog-loss = ",l,"\nF-score = ", svc_f)

noiz=np.random.normal(0, 0.2, 64)
noiz_train=np.zeros((70,64))
noiz_test=np.zeros((30,64))

for i in range(len(x_train)):
    noiz_train[i]=x_train[i]+noiz
for i in range(len(x_test)):
    noiz_test[i]=x_test[i]+noiz

new_train=medfilt(noiz_train)
new_test=medfilt(noiz_test)


svc = SVC(probability=True)
tr=svc.fit(noiz_train, y_train)

svc_m=confusion_matrix(y_test,tr.predict(noiz_test))
svc_farn=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])
svc_frrn = svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])
svc_prn = tr.predict_proba(noiz_test)
ln = log_loss(y_test,svc_prn)

svc_fn=f1_score(y_test,tr.predict(noiz_test))
print("after noise: ")
print("FAR =", svc_farn, "\nFRR = ",svc_frrn,"\nlog-loss = ",ln,"\nF-score = ", svc_fn)


