import numpy as np
import pywt
import scipy.fft as fft
import csv
x = []
with open('gyro_proba.csv') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        x.append(row["x"])
f = np.abs(fft.fft(x))
print(pywt.swt(x[:-1],'db1'))
