import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.multiclass import OneVsRestClassifier
#binar
def l_reg(x_train,y_train,x_test,y_test):
    log=LogisticRegression()
    m=log.fit(x_train, y_train)
    con_matr= confusion_matrix(y_test, m.predict(x_test))
    lregFAR=con_matr[0][1]/(con_matr[0][1] + con_matr[0][0]) 
    lregFRR=con_matr[1][0]/(con_matr[1][1] + con_matr[1][0]) 
    predic=m.predict_proba(x_test)
    log_l= log_loss(y_test, predic) 
    f1= f1_score(y_test, m.predict(x_test))  
    print('FAR =',lregFAR ,'FRR =', lregFRR,'log-loss = ', log_l,'F-score = ',f1)
def supVecMa(x_train,y_train,x_test,y_test):
    svc = SVC(probability=True)
    m=svc.fit(x_train, y_train)

    con_matr= confusion_matrix(y_test,m.predict(x_test))
    svcFAR= con_matr[0][1]/(con_matr[0][1]+con_matr[0][0])
    svcFRR= con_matr[1][0]/(con_matr[1][1]+con_matr[1][0])

    predic= m.predict_proba(x_test)
    log_l= log_loss(y_test,predic) 

    f1= f1_score(y_test,m.predict(x_test))

    print('FAR =',svcFAR ,'FRR =', svcFRR,'log-loss = ', log_l,'F-score = ',f1)
def forest(x_train,y_train,x_test,y_test):
    tree = DecisionTreeClassifier()
    m= tree.fit(x_train, y_train)

    con_matr= confusion_matrix(y_test,m.predict(x_test))
    tFAR = con_matr[0][1]/(con_matr[0][1]+con_matr[0][0])
    tFRR = con_matr[1][0]/(con_matr[1][1]+con_matr[1][0])

    predic= m.predict_proba(x_test)
    log_l = log_loss(y_test,predic) 

    f1 = f1_score(y_test,m.predict(x_test))

    print('FAR =',tFAR ,'FRR =', tFRR,'log-loss = ', log_l,'F-score = ',f1)
#multiclass
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
    
