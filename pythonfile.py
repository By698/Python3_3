import numpy as np

values = np.loadtxt('iris.data', delimiter=',', usecols=[0, 1, 2, 3])
labels = np.loadtxt('iris.data', dtype='U15', delimiter=',', usecols=[4])
#    1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class


sepal_length, sepal_width, petal_length, petal_width = values.T
iris_class = labels.T


def srednia_arytmetyczna(dana):
    avg = np.average(dana)

    return avg


def odchylenie_standardowe(dana):
    std = np.std(sepal_length)

    return std

def mediana(dana):
    median = np.median(dana)

    return median


def minimum(dana):
    min = np.minimum(dana)

    return min


def maximum(dana):
    max = np.maximum(dana)

    return max
