import numpy as np
import csv
from scipy.stats import ks_2samp
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

def unigr(file_name):
    f = open(file_name, newline='')
    reader = csv.reader(f)
    unigram=[]
    a=0
    for row in reader:
        n=len(row)
        k=3
        if a>0 and a<=15:
            while k<=n-2:
                unigram.append([float(row[k]),float(row[k+1])])
                k+=3
        a+=1
    return unigram

def col(unigrama):
    n=len(unigrama)
    c=[]
    for i in range(0,n):
        c.append(unigrama1[i][0])
    c=np.array(c)
    return c


unigrama1 = np.array(unigr("date.csv"))
unigrama2 = np.array(unigr("novikova.csv"))

i1=np.zeros(len(unigrama1),dtype=int)
i2=np.ones(len(unigrama1),dtype=int)



unigram=np.row_stack((unigrama1,unigrama2))
i=np.hstack((i1,i2))


colum=col(unigrama1)
n=len(colum)



x = np.random.normal(0, 1, n)

s,p=ks_2samp(colum, x)
print(ks_2samp(colum, x))
alpha=0.05
flag=''
if p > alpha:
    flag='Sample looks Gaussian (fail to reject H0)'
else:
    flag='Sample does not look Gaussian (reject H0)'

#logistic regressions
logreg_clf = LogisticRegression()
logreg_clf.fit(unigram, i)

logreg_m=confusion_matrix(i,logreg_clf.predict(unigram))
logreg_far=logreg_m[0][1]/(logreg_m[0][1]+logreg_m[0][0])#FAR
logreg_frr=logreg_m[1][0]/(logreg_m[1][1]+logreg_m[1][0])#FRR
#print(logreg_m)
#print(logreg_far,logreg_frr)

log_pr=logreg_clf.predict_proba(unigram)#ефективність моделі
l1=log_loss(i,log_pr) #log-loss metrics
#print(l1)

i_p1=(logreg_clf.predict(unigram))# фактичні прогнози
log_f=f1_score(i,i_p1)#F-score
#print(log_f)

#print(logreg_clf.score(unigram, i))#точність моделі
print("Логістична регресія  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(logreg_far,logreg_frr,l1,log_f))

#support vector machine
svc = SVC(probability=True)
svc.fit(unigram, i)

svc_m=confusion_matrix(i,svc.predict(unigram))
svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR
#print(svc_m)
#print(svc_far,svc_frr)

svc_pr=svc.predict_proba(unigram)#ефективність моделі
l2=log_loss(i,svc_pr) #log-loss metrics
#print(l2)

i_p2=(svc.predict(unigram))# фактичні прогнози
svc_f=f1_score(i,i_p2)#F-score
#print(svc_f)

#print(svc.score(unigram, i))#точність моделі
print("Опорна векторна машина  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))



#ensemble of Linear Fisher Discriminants (random forest)
tree = DecisionTreeClassifier()
tree.fit(unigram, i)

tree_m=confusion_matrix(i, tree.predict(unigram))
tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR
#print(tree_m)
#print(tree_far,tree_frr)

tree_pr=tree.predict_proba(unigram)#ефективність моделі
l3=log_loss(i,tree_pr) #log-loss metrics
#print(l3)

i_p3=tree.predict(unigram)# фактичні прогнози
tree_f=f1_score(i,i_p3)#F-score
#print(tree_f)

#print(tree.score(unigram, i))#точність моделі

print("Випадковий ліс  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l3,tree_f))

