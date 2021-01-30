from sklearn.datasets import load_digits
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot
import numpy as np

digits = load_digits()
data = digits.data
target = digits.target

fig = plot.figure(figsize=(6, 6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], interpolation='nearest')
    ax.text(0, 7, str(digits.target[i]))
plot.show()

normalized_data = preprocessing.normalize(data)
print("normalized_data.shape: ", normalized_data.shape)
n_samples = len(normalized_data)
flattened_data = digits.images.reshape((n_samples, -1)) #np.ravel()
print("flattened_data.shape: ", flattened_data.shape)
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=30, train_size=70, shuffle=True)
# print("x_train.shape: ", x_train.shape, " y_train.shape: ", y_train.shape, " np.ravel(y_train): ", np.ravel(y_train, order=None).shape)
classifier = svm.SVC(kernel='linear')
classifier = classifier.fit(x_train, y_train)
print("x_test.shape: ", x_test.shape)

prediction = classifier.predict(x_test)
print("prediction: ", prediction)
print("The measure of accuracy (coefficient of determination) for training: ",classifier.score(x_train, y_train))
print("The measure of accuracy (coefficient of determination) for test: ", classifier.score(x_test, y_test))

noise = np.random.normal(0, 0.2, 30)
prediction = classifier.predict(x_test + noise.reshape(-1, 1))
print("prediction with noise: ", prediction)
print("The measure of accuracy (coefficient of determination) for noised test: ", classifier.score(x_test + noise.reshape(-1, 1), y_test))