import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.multiclass import OneVsRestClassifier





def mul_svc_test(x_train ,y_train ,x_test ,y_test):
    svc = OneVsRestClassifier(SVC(probability=True))
    tr = svc.fit(x_train, y_train)
     
    svc_pr = tr.predict_proba(x_test) 
    ll = log_loss(y_test ,svc_pr) 
    svc_f = f1_score(y_test ,tr.predict(x_test),average = 'weighted')  
    print('log-loss = ', ll)
    print('F-score = ', svc_f)

    

def mul_log_test(x_train,y_train,x_test,y_test):
    log = OneVsRestClassifier(LogisticRegression())
    tr = log.fit(x_train, y_train)
    log_pr = tr.predict_proba(x_test) 
    ll = log_loss(y_test, log_pr)  
    log_f = f1_score(y_test, tr.predict(x_test),average = 'weighted') 
    print('log-loss = ', ll)
    print('F-score = ', log_f)

def multi_forest_test(x_train,y_train,x_test,y_test):
    tree = OneVsRestClassifier(DecisionTreeClassifier())
    tr = tree.fit(x_train, y_train)
    tree_pr = tr.predict_proba(x_test)
    ll = log_loss(y_test,tree_pr) 
    tree_f = f1_score(y_test,tr.predict(x_test),average = 'weighted')

    print('log-loss = ', ll)
    print('F-score = ', tree_f)
    
    
