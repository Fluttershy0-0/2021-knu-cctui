from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score,roc_curve
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.multiclass import OneVsRestClassifier


def multi_svc_test(x_train ,y_train ,x_test ,y_test):
    svc = OneVsRestClassifier(SVC(probability=True))
    tr =svc.fit(x_train, y_train)

    svc_pr =tr.predict_proba(x_test)  # ефективність моделі
    l2 =log_loss(y_test ,svc_pr)  # log-loss metrics

    #svc_far, tpr, thresholds = roc_curve(y_test, svc_pr)
    #svc_frr = 1 - tpr  # FRR

    #print(svc_pr)
    svc_f =f1_score(y_test ,tr.predict(x_test),average='weighted')  # F-score


    print("Multiclass classification SVC   log-loss={} ,F-score={} ".format(l2,svc_f))

def multi_log_test(x_train,y_train,x_test,y_test):
    log =OneVsRestClassifier(LogisticRegression())
    tr = log.fit(x_train, y_train)

    log_m = confusion_matrix(y_test, tr.predict(x_test))
    #log_far = log_m[0][1] / (log_m[0][1] + log_m[0][0])  # FAR
    #log_frr = log_m[1][0] / (log_m[1][1] + log_m[1][0])  # FRR

    log_pr = tr.predict_proba(x_test)  # ефективність моделі
    l2 = log_loss(y_test, log_pr)  # log-loss metrics

    log_f = f1_score(y_test, tr.predict(x_test),average='weighted')  # F-score

    print("Multiclass classification Логістична регресія   log-loss={} ,F-score={} ".format(l2, log_f))

def multi_forest_test(x_train,y_train,x_test,y_test):
    tree = OneVsRestClassifier(DecisionTreeClassifier())
    tr=tree.fit(x_train, y_train)

    tree_m=confusion_matrix(y_test,tr.predict(x_test))
    #tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
    #tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR

    tree_pr=tr.predict_proba(x_test)#ефективність моделі
    l2=log_loss(y_test,tree_pr) #log-loss metrics

    tree_f=f1_score(y_test,tr.predict(x_test),average='weighted')#F-score

    print("Multiclass classification Випадковий ліс  log-loss={} ,F-score={} ".format(l2,tree_f))