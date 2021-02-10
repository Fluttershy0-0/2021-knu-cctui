from zipfile import ZipFile
import numpy as np
import pandas as pd
from scipy import signal
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

zip_file = ZipFile('1-digit-session-2.zip')
dfs = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename))
       for text_file in zip_file.infolist()
       if text_file.filename.endswith('.csv')}


def get_data_values():
    dict_keys = list(dfs.keys())
    data = {}
    series_names = []
    for key in dict_keys:
        split = key.split("_")
        if len(split) > 1:
            series_type = split[0]
            series_name = split[1].split(".")[0]
            if series_name not in series_names:
                series_names.append(series_name)
                data[series_name] = {}
            datum = data[series_name]
            datum[series_type] = dfs[key]
    return data.values()


def apply_filters(signal_noisy):
    signal_median = signal.medfilt(signal_noisy)
    return signal.savgol_filter(signal_median, 7, 3, mode='nearest')


def get_dataset(dataset, size, key_val, acc, gyro):
    for i in range(0, size):
        new_set = []
        new_set.append(str(key_val))
        new_set.append((acc[i])[0])
        new_set.append((acc[i])[1])
        new_set.append((acc[i])[2])
        new_set.append((gyro[i])[0])
        new_set.append((gyro[i])[1])
        new_set.append((gyro[i])[2])
        dataset.append(new_set)


def segment(dataset, key, acc, gyro):
    key_val = key.loc[0]
    acc_c = apply_filters(acc.drop(columns=['timestamp']))
    gyro_c = apply_filters(gyro.drop(columns=['timestamp']))
    size = min(len(acc), len(gyro))  # full size ~450 samples, use it if you have a lot of time
    quick_size = size
    get_dataset(dataset, quick_size, key_val, acc_c, gyro_c)
    # print(len(dataset))
    # print(dataset)


def define_value(n, counter):
    if n == '0':
        counter[0] += 1
    elif n == '1':
        counter[1] += 1
    elif n == '2':
        counter[2] += 1
    elif n == '3':
        counter[3] += 1
    elif n == '4':
        counter[4] += 1
    elif n == '5':
        counter[5] += 1
    elif n == '6':
        counter[6] += 1
    elif n == '7':
        counter[7] += 1
    elif n == '8':
        counter[8] += 1
    elif n == '9':
        counter[9] += 1


def count_entries(array):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in array:
        if isinstance(i, np.ndarray):
            n = str(int(i[0]))
            define_value(n, counter)
        elif isinstance(i, int) or isinstance(i, float):
            n = str(int(i))
            define_value(n, counter)
    print("0:", counter[0], " 1:", counter[1], " 2:", counter[2], " 3:", counter[3], " 4:", counter[4],
          " 5:", counter[5], " 6:", counter[6], " 7:", counter[7], " 8:", counter[8], " 9:", counter[9])
    return counter


# prepare data
#
# attention: takes a lot of time!
# run it on your risk or use saved data
#
dataset = []
for data_table in get_data_values():
    key = data_table.get('key').get('key')
    acc = data_table.get('acc')
    gyro = data_table.get('gyro')
    segment(dataset, key, acc, gyro)
data_size = len(dataset)
print("\ndataset size: ", data_size)
arr = np.array(dataset)
print("Before shuffle:")
count_entries(arr)
np.random.shuffle(arr)
print("After shuffle:")
count_entries(arr)
# train_size = data_size - data_size // 20
# verify_size = (data_size - train_size) // 2
# training, verification, test = np.split(arr, [train_size, train_size + verify_size])
training = arr
verification, test = np.split(arr, [data_size // 4])

pd.DataFrame(training).to_csv("training.csv", header=None, index=None)
pd.DataFrame(verification).to_csv("verification.csv", header=None, index=None)
pd.DataFrame(test).to_csv("test.csv", header=None, index=None)

# read test
#
training = pd.read_csv("training.csv", header=None).to_numpy()
verification = pd.read_csv("verification.csv", header=None).to_numpy()
# test = pd.read_csv("test.csv", header=None).to_numpy()
print("\ntraining size: ", len(training))
count_entries(training)
print("\nverification size: ", len(verification))
ver_count = count_entries(verification)
# print("\ntest size: ", len(test))
# tst_count = count_entries(test)

# training
#
# expected_labels = []
# for i in range(0, 10):
#     expected_labels.append(str(i[0]))
# print("expected_labels: ", expected_labels)
y, x = np.hsplit(training, [1])
y = np.ravel(y)
vy, vx = np.hsplit(verification, [1])
vy = np.ravel(vy)
# ty, tx = np.hsplit(test, [1])
# ty = np.ravel(ty)

print("\nSVM")
svm_classifier = svm.SVC()
svm_classifier = svm_classifier.fit(x, y)

# print("\nexpected labels training: \n", y)
# count_entries(y)
# prediction_svm_training = svm_classifier.predict(x)
# print("prediction svm training: \n", prediction_svm_training)
# count_entries(prediction_svm_training)
# accuracy_rate_svm_training = accuracy_score(y, prediction_svm_training, normalize=True)
# print("accuracy rate svm training: ", accuracy_rate_svm_training)

print("\nexpected labels verification: \n", vy)
count_entries(vy)
prediction_svm_verification = svm_classifier.predict(vx)
print("prediction_svm_verification: \n", prediction_svm_verification)
count_entries(prediction_svm_verification)
accuracy_rate_svm_verification = accuracy_score(vy, prediction_svm_verification, normalize=True)
print("accuracy rate svm verification: ", accuracy_rate_svm_verification)

print("\nLogisticRegression")
regression_model = LogisticRegression()
regression_model = regression_model.fit(x, y)

# print("\nexpected labels training: \n", y)
# count_entries(y)
# prediction_lr_training = regression_model.predict(x)
# print("prediction regression training \n", prediction_lr_training)
# count_entries(prediction_lr_training)
# accuracy_rate_lr_training = accuracy_score(y, prediction_lr_training, normalize=True)
# print("accuracy rate lr training: ", accuracy_rate_lr_training)

print("\nexpected labels verification: \n", vy)
count_entries(vy)
prediction_lr_verification = regression_model.predict(vx)
print("prediction regression verification \n", prediction_lr_verification)
count_entries(prediction_lr_verification)
accuracy_rate_lr_verification = accuracy_score(vy, prediction_lr_verification, normalize=True)
print("accuracy rate lr verification: ", accuracy_rate_lr_verification)

print("\nRandomForest")
classifier_rf = RandomForestClassifier(n_estimators=100)
classifier_rf = classifier_rf.fit(x, y)

print("\nexpected labels verification: \n", vy)
count_entries(vy)
prediction_rf_verification = classifier_rf.predict(vx)
print("prediction RandomForest verification \n", prediction_rf_verification)
count_entries(prediction_rf_verification)
accuracy_rate_rf_verification = accuracy_score(vy, prediction_rf_verification, normalize=True)
print("accuracy rate RandomForest verification: ", accuracy_rate_rf_verification)

# print("pin with lr: ", regression_model.predict(np.array(test_pin).reshape(1, -1)))
