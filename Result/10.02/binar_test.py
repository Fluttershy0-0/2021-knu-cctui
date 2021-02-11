from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,log_loss,f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.multiclass import OneVsRestClassifier



#dig_train, dig_test, i_train, i_test = train_test_split(All_dig, All_i, test_size=0.3, random_state=42)


def log_test(x_train,y_train,x_test,y_test):
    log = LogisticRegression()
    tr = log.fit(x_train, y_train)

    log_m = confusion_matrix(y_test, tr.predict(x_test))
    log_far = log_m[0][1] / (log_m[0][1] + log_m[0][0])  # FAR
    log_frr = log_m[1][0] / (log_m[1][1] + log_m[1][0])  # FRR

    log_pr = tr.predict_proba(x_test)  # ефективність моделі
    l2 = log_loss(y_test, log_pr)  # log-loss metrics

    log_f = f1_score(y_test, tr.predict(x_test))  # F-score

    print("Логістична регресія  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(log_far, log_frr, l2, log_f))


def svc_test(x_train,y_train,x_test,y_test):
    svc = SVC(probability=True)
    tr=svc.fit(x_train, y_train)

    svc_m=confusion_matrix(y_test,tr.predict(x_test))
    svc_far=svc_m[0][1]/(svc_m[0][1]+svc_m[0][0])#FAR
    svc_frr=svc_m[1][0]/(svc_m[1][1]+svc_m[1][0])#FRR

    svc_pr=tr.predict_proba(x_test)#ефективність моделі
    l2=log_loss(y_test,svc_pr) #log-loss metrics

    svc_f=f1_score(y_test,tr.predict(x_test))#F-score

    print("Опорна векторна машина  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(svc_far,svc_frr,l2,svc_f))


def forest_test(x_train,y_train,x_test,y_test):
    tree = DecisionTreeClassifier()
    tr=tree.fit(x_train, y_train)

    tree_m=confusion_matrix(y_test,tr.predict(x_test))
    tree_far=tree_m[0][1]/(tree_m[0][1]+tree_m[0][0])#FAR
    tree_frr=tree_m[1][0]/(tree_m[1][1]+tree_m[1][0])#FRR

    tree_pr=tr.predict_proba(x_test)#ефективність моделі
    l2=log_loss(y_test,tree_pr) #log-loss metrics

    tree_f=f1_score(y_test,tr.predict(x_test))#F-score

    print("Випадковий ліс  FAR={}, FRR={}, log-loss={} ,F-score={} ".format(tree_far,tree_frr,l2,tree_f))



