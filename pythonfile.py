import numpy as np

values = np.loadtxt('iris.data', delimiter=',', usecols=[0, 1, 2, 3])
labels = np.loadtxt('iris.data', dtype='U15', delimiter=',', usecols=[4])

sepal_length, sepal_width, petal_length, petal_width = values.T
iris_class = labels.T


def dane_ilosciowe(dana, name):
    avg = np.average(dana)
    std = np.std(sepal_length)
    median = np.median(dana)
    min = np.minimum(dana)
    max = np.maximum(dana)

    print('Średnia arytmetyczna', name, ' to:', avg)
    print('Odchylenie standardowe', name, ' to:', std)
    print('Mediana', name, ' to:', median)
    print('Najmniejsza wartosc', name, ' to:', min)
    print('Najwieksza wartosc', name, ' to:', max)


dane_ilosciowe(sepal_length, 'sepal_length')