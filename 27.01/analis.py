import numpy as np
import csv
from scipy.stats import ks_2samp
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

def unigramram(file_name):
    f = open(file_name, newline='')
    reader = csv.reader(f)
    unigramram=[]
    a=0
    for row in reader:
        n=len(row)
        k=3
        if a>0 and a<=15:
            while k<=n-2:
                unigramram.append([float(row[k]),float(row[k+1])])
                k+=3
        a+=1
    return unigramram

def collected(unigramrama):
    n=len(unigramrama)
    c=[]
    for i in range(0,n):
        c.append(strongpassworddata[i][0])
    c=np.array(c)
    return c


strongpassworddata = np.array(unigramram("date.csv"))
strongpassworddatatwo= np.array(unigramram("DSL-StrongPasswordData.csv"))

i1=np.zeros(len(strongpassworddata),dtype=int)
i2=np.ones(len(strongpassworddata),dtype=int)



unigramram=np.row_stack((strongpassworddata,strongpassworddatatwo))
i=np.hstack((i1,i2))


collectum=collected(strongpassworddata)
n=len(collectum)



x = np.random.normal(0, 1, n)
print("Обчислення статистики Колмогорова-Смірнова за 2 зразками.");
s,p=ks_2samp(collectum, x)
print(ks_2samp(collectum, x))
alpha=0.05
# classifiers:logit model
logreg_clf = LogisticRegression()
logreg_clf.fit(unigramram, i)
logreg_m=confusion_matrix(i,logreg_clf.predict(unigramram))
logreg_far=logreg_m[0][1]/(logreg_m[0][1]+logreg_m[0][0])#FAR
logreg_frr=logreg_m[1][0]/(logreg_m[1][1]+logreg_m[1][0])#FRR
log_pr=logreg_clf.predict_proba(unigramram)#ефективність моделі
l1=log_loss(i,log_pr) #log-loss metrics
i_p1=(logreg_clf.predict(unigramram))# фактичні прогнози
log_f=f1_score(i,i_p1)#F-score



#support vector machine
svc = SVC(probability=True)
svc.fit(unigramram, i)
svc_m=confusion_matrix(i,svc.predict(unigramram))
svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR
svc_pr=svc.predict_proba(unigramram)#ефективність моделі
l2=log_loss(i,svc_pr) #log-loss metrics
i_p2=(svc.predict(unigramram))# фактичні прогнози
svc_f=f1_score(i,i_p2)#F-score





#random forest
tree = DecisionTreeClassifier()
tree.fit(unigramram, i)
tree_m=confusion_matrix(i, tree.predict(unigramram))
tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR
tree_pr=tree.predict_proba(unigramram)#ефективність
l3=log_loss(i,tree_pr) #log-loss metrics
i_p3=tree.predict(unigramram)#  прогнози
tree_f=f1_score(i,i_p3)#F-score



print("Випадковий ліс  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l3,tree_f))
print((len(("Випадковий ліс  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l3,tree_f))))*"-")

print("Опорна векторна машина  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))
print((len(("Опорна векторна машина  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))))*"-")


print("Логістична регресія  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(logreg_far,logreg_frr,l1,log_f))
print((len(("Логістична регресія  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(logreg_far,logreg_frr,l1,log_f))))*"-")
