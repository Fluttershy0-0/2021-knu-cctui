from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score,multilabel_confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.multiclass import OneVsRestClassifier
import numpy as np




def multi_svc_test(x_train ,y_train ,x_test ,y_test):
    svc = OneVsRestClassifier(SVC(probability=True))
    tr =svc.fit(x_train, y_train)

    svc_m = multilabel_confusion_matrix(y_test, tr.predict(x_test), labels=np.arange(0,10))
    svc_pr =tr.predict_proba(x_test)  # ефективність моделі
    l2 =log_loss(y_test ,svc_pr)  # log-loss metrics


    svc_f =f1_score(y_test ,tr.predict(x_test),average='weighted')  # F-score


    print("Multiclass classification SVC confusion matrix={}  log-loss={} ,F-score={} ".format(svc_m,l2,svc_f))





def multi_log_test(x_train,y_train,x_test,y_test):
    log =OneVsRestClassifier(LogisticRegression())
    tr = log.fit(x_train, y_train)

    log_m = multilabel_confusion_matrix(y_test, tr.predict(x_test), labels=np.arange(0,10))

    log_pr = tr.predict_proba(x_test)  # ефективність моделі
    print(log_pr)
    print(y_test)
    l2 = log_loss(y_test, log_pr)  # log-loss metrics

    log_f = f1_score(y_test, tr.predict(x_test),average='weighted')  # F-score

    print("Multiclass classification Логістична регресія confusion matrix={}  log-loss={} ,F-score={} ".format(log_m,l2, log_f))




def multi_forest_test(x_train,y_train,x_test,y_test):
    tree = OneVsRestClassifier(DecisionTreeClassifier())
    tr=tree.fit(x_train, y_train)

    tree_m=multilabel_confusion_matrix(y_test, tr.predict(x_test), labels=np.arange(0,10))

    tree_pr=tr.predict_proba(x_test)#ефективність моделі

    l2=log_loss(y_test,tree_pr) #log-loss metrics

    tree_f=f1_score(y_test,tr.predict(x_test),average='weighted')#F-score

    print("Multiclass classification Випадковий ліс confusion matrix={} log-loss={} ,F-score={} ".format(tree_m,l2,tree_f))