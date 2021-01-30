import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from iteration_utilities import deepflatten
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy import ndimage, misc
from scipy.signal import medfilt2d
import scipy.signal as signal
from scipy import ndimage
digits = datasets.load_digits()
n_s=len(digits.images)
data=digits.images.reshape((n_s, -1))
#noise = np.random.normal(0,0.2,np.shape(data))
#data_noised=data+noise
#data=ndimage.median_filter(data_noised,size=(3,7))
cl=svm.SVC(gamma=0.001)
X_train, X_test, y_train, y_test = train_test_split(data, digits.target, test_size=0.3,train_size=0.7,random_state=10, shuffle=True)
#X_train=MinMaxScaler().fit_transform(X_train)
#X_test=MinMaxScaler().fit_transform(X_test)
cl.fit(X_train, y_train)
predicted = cl.predict(X_test)
_,axes =plt.subplots(nrows=1,ncols=4,figsize=(10, 3))
for ax, image, prediction in zip(axes,X_test,predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')
print(f"Classification report for classifier {cl}:\n" f"{metrics.classification_report(y_test, predicted)}\n")
disp = metrics.plot_confusion_matrix(cl, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()
