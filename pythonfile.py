import numpy as np
from scipy.stats import mode
values = np.loadtxt('iris.data', delimiter=',', usecols=[0, 1, 2, 3])
labels = np.loadtxt('iris.data', dtype='U15', delimiter=',', usecols=[4])

sepal_length, sepal_width, petal_length, petal_width = values.T
iris_class = labels.T


def dominant(data):
    _ = mode(data)

    print('Najczęściej występująca wartość to:', _[0][0])
    print('Liczebność:', _[1][0])
    print('Częstość:', _[1][0] / len(data))

