import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score



def log_test(x_train,y_train,x_test,y_test):
    log = LogisticRegression()
    tr = log.fit(x_train, y_train)

    log_m = confusion_matrix(y_test, tr.predict(x_test))
    log_far = log_m[0][1] / (log_m[0][1] + log_m[0][0]) 
    log_frr = log_m[1][0] / (log_m[1][1] + log_m[1][0]) 

    log_pr = tr.predict_proba(x_test)
    ll = log_loss(y_test, log_pr) 

    log_f = f1_score(y_test, tr.predict(x_test))  

    print('FAR =', log_far)
    print('FRR =', log_frr)
    print('log-loss = ', ll)
    print('F-score = ', log_f)

def svc_test(x_train,y_train,x_test,y_test):
    svc = SVC(probability=True)
    tr = svc.fit(x_train, y_train)

    svc_m = confusion_matrix(y_test,tr.predict(x_test))
    svc_far = svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])
    svc_frr = svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])

    svc_pr = tr.predict_proba(x_test)
    ll = log_loss(y_test,svc_pr) 

    svc_f = f1_score(y_test,tr.predict(x_test))

    print('FAR =', svc_far)
    print('FRR =', svc_frr)
    print('log-loss = ', ll)
    print('F-score = ', svc_f)


def forest_test(x_train,y_train,x_test,y_test):
    tree = DecisionTreeClassifier()
    tr = tree.fit(x_train, y_train)

    tree_m = confusion_matrix(y_test,tr.predict(x_test))
    tree_far = tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])
    tree_frr = tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])

    tree_pr = tr.predict_proba(x_test)
    ll = log_loss(y_test,tree_pr) 

    tree_f = f1_score(y_test,tr.predict(x_test))

    print('FAR =', tree_far)
    print('FRR =', tree_frr)
    print('log-loss = ', ll)
    print('F-score = ', tree_f)








