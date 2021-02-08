from zipfile import ZipFile
import numpy as np
import pandas as pd
from scipy import signal
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

zip_file = ZipFile('1-digit-session-1.zip')
dfs = {text_file.filename: pd.read_csv(zip_file.open(text_file.filename))
       for text_file in zip_file.infolist()
       if text_file.filename.endswith('.csv')}

def prepare_data_values():
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

def filter_noise(signal_noisy):
  signal_median = signal.medfilt(signal_noisy)
  return signal.savgol_filter(signal_median, 3, 2, mode='mirror')

def time_align(dataset, size, key_val, acc, gyro):
  for i in range(0, size):
    new_set = []
    new_set.append(key_val)
    new_set.append((acc[i])[0])
    new_set.append((acc[i])[1])
    new_set.append((acc[i])[2])
    new_set.append((gyro[i])[0])
    new_set.append((gyro[i])[1])
    new_set.append((gyro[i])[2])
    dataset.append(new_set)

def segmentate(dataset, key, acc, gyro):
  key_val = key.loc[0]
  acc_c = filter_noise(acc.drop(columns=['timestamp']))
  gyro_c = filter_noise(gyro.drop(columns=['timestamp']))
  size = min(len(acc), len(gyro)) # full size ~450 samples, use it if you have a lot of time
  quick_training_size = 50
  time_align(dataset, quick_training_size, key_val, acc_c, gyro_c)
  print(len(dataset))

dataset = []
for data_table in prepare_data_values():
  key = data_table.get('key').get('key')
  acc = data_table.get('acc')
  gyro = data_table.get('gyro')
  segmentate(dataset, key, acc, gyro)

print(dataset[1])
arr = np.array(dataset)
y, x = np.hsplit(arr, [1])
y = np.ravel(y)

svm_classifier = svm.SVC(kernel='linear')
svm_classifier = svm_classifier.fit(x, y)
prediction_svm = svm_classifier.predict(x)
print("svm_classifier \n", prediction_svm)
regression_model = LogisticRegression(max_iter=10000)
regression_model = regression_model.fit(x, y)
prediction_lr = regression_model.predict(x)
print("regression_model \n", prediction_lr)
one_vs_rest = OneVsRestClassifier(svm.SVC())
one_vs_rest = one_vs_rest.fit(x, y)
prediction_one = one_vs_rest.predict(x)
print("one_vs_rest \n", prediction_one)
