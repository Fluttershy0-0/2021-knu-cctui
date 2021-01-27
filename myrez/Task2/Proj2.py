import pandas as pd
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

data = pd.read_csv('DSL-StrongPasswordData.csv')
data.drop('sessionIndex', axis=1, inplace=True)
data.drop('rep', axis=1, inplace=True)
#print(data.head(3))
for i in range(1, 32):
    if (i+1) % 3 != 1:
        data.drop(data.columns[[32 - i]], axis=1, inplace=True)
#print(data.head(3))


# print(data.head(5))

# ".iloc" принимает row_indexer, column_indexer
X = data.iloc[:, 1:100].values
# Теперь выделим нужный столбец
y = data['subject']
# print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=27)

# print(X_train)
# print(y_train)
print("Unigram efficiency:")
"""
print("SVC method:")
SVC_model = svm.SVC()
SVC_model.fit(X_train, y_train)
SVC_prediction = SVC_model.predict(X_test)
print(accuracy_score(SVC_prediction, y_test))
print(confusion_matrix(SVC_prediction, y_test))

print("Logistic regression method:")
logreg_clf = LogisticRegression()
logreg_clf.fit(X_train, y_train)
logreg_prediction = logreg_clf.predict(X_test)
print(accuracy_score(logreg_prediction, y_test))
print(confusion_matrix(logreg_prediction, y_test))
"""

print("Random Forest method:")
RF_model = RandomForestClassifier()
RF_model.fit(X_train, y_train)
RF_prediction = RF_model.predict(X_test)
print(accuracy_score(RF_prediction, y_test))
print(confusion_matrix(RF_prediction, y_test))

