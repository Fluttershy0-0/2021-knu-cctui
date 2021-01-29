import csv
import numpy
from scipy import stats
from sklearn.calibration import CalibratedClassifierCV
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB

f_gathered = open("keystroke_dynamics_final_dataset.csv", "r")
f_training = open("DSL-StrongPasswordData.csv", "r")
classes = []
training_set = []
gathered_set = []

def read_single_column(x, file, title, max_size):
    reader = csv.DictReader(file)
    for row in reader:
        x.append(row[title])
        if len(x) == max_size:
            return

def read_multiple_columns(file, x, title1, xx, titles, max_size):
    reader = csv.DictReader(file)
    for row in reader:
        w = []
        for title in titles:
            w.append(float(row[title]))
        xx.append(w)
        x.append(row[title1])
        if len(xx) == max_size:
            return

def kolmogorov_smirnov():
    x1 = []
    x2 = []
    read_single_column(x1, f_gathered, 'H.period', 30)
    f_gathered.seek(0)
    read_single_column(x2, f_training, 'H.period', 30)
    f_training.seek(0)
    print(x1)
    print(x2)
    print("\nKolmogorov-Smirnov:")
    print("normal distribution: ", stats.kstest(stats.norm.rvs, 'norm'))
    print("gathered dataset: ", stats.kstest(numpy.asarray(x1, dtype=numpy.float), 'norm'))
    print("training dataset: ", stats.kstest(numpy.asarray(x2, dtype=numpy.float), 'norm'))

def get_classification_datasets():
    unigrams = ['DD.period.t', 'DD.t.i', 'DD.i.e', 'DD.e.five', 'DD.five.Shift.r',
                'DD.Shift.r.o', 'DD.o.a', 'DD.a.n', 'DD.n.l']

    read_multiple_columns(f_training, classes, 'subject', training_set, unigrams, 4000)
    f_training.seek(0)

    print("\nRetrieving classification datasets")
    print("Size classes: ", len(classes), ", sample:", classes[:10])
    print("Size training_set: ", len(training_set), ", sample:", training_set[0])
    empty = []
    read_multiple_columns(f_gathered, empty, 'sessionIndex', gathered_set, unigrams, -1)
    print("Size gathered_set: ", len(gathered_set), ", sample:", gathered_set[0])
    f_gathered.seek(0)

def logistic_regression():
    reg = LogisticRegression().fit(training_set, classes)

    print("\nLogistic Regression")
    print("Predict class labels for samples in X: ", reg.predict(gathered_set))
    print("Probability estimates: ", reg.predict_proba(gathered_set))
    print("Mean accuracy on the given test data and labels: ", reg.score(training_set, classes))

def svm_classification():
    clf = svm.SVC()
    clf.fit(training_set, classes)

    print("\nSVM Classification")
    print("Predict class labels for samples in X: ", clf.predict(gathered_set))
    clc = GaussianNB()
    clc.fit(training_set, classes)  # GaussianNB itself does not support sample-weights
    print("Probability estimates: ", clc.predict_proba(gathered_set))

def random_forest():
    clf = RandomForestClassifier(max_depth=4, random_state=0)
    clf.fit(training_set, classes)

    print("\nRandom Forest")
    print("Predict class labels for samples in X: ", clf.predict(gathered_set))
    print("Probability estimates: ", clf.predict_proba(gathered_set))

kolmogorov_smirnov()
get_classification_datasets()
logistic_regression()
svm_classification()
random_forest()
f_gathered.close()
f_training.close()