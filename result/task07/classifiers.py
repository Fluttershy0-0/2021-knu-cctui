from sklearn.datasets import make_classification
from sklearn import svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

x, y = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)


classifier = svm.SVC(kernel='linear')
classifier = classifier.fit(x, y)
prediction = classifier.predict(x)
print("svm \n", prediction)
classifier_lr = LogisticRegression(max_iter=10000)
classifier_lr = classifier_lr.fit(x, y)
prediction_lr = classifier_lr.predict(x)
print("lr \n", prediction_lr)
classifier_rf = RandomForestClassifier()
classifier_rf = classifier_rf.fit(x, y)
prediction_rf = classifier_rf.predict(x)
print("rf \n", prediction_rf)

xm, ym = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
clf = OneVsRestClassifier(svm.SVC())
clf.fit(xm, ym)
print("\nmulticlass\n", clf.predict(x))
