import numpy as np
from scipy.stats import mode
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
values = np.loadtxt('iris.data', delimiter=',', usecols=[0, 1, 2, 3])
labels = np.loadtxt('iris.data', dtype='U15', delimiter=',', usecols=[4])

sepal_length, sepal_width, petal_length, petal_width = values.T
iris_class = labels.T


def dominant(data):
    _ = mode(data)

    print('Najczęściej występująca wartość to:', _[0][0])
    print('Liczebność:', _[1][0])
    print('Częstość:', _[1][0] / len(data))


def dane_ilosciowe(dana, name):
    avg = np.average(dana)
    std = np.std(sepal_length)
    median = np.median(dana)
    min = np.amin(dana)
    max = np.amax(dana)

    print('Średnia arytmetyczna', name, ' to:', avg)
    print('Odchylenie standardowe', name, ' to:', std)
    print('Mediana', name, ' to:', median)
    print('Najmniejsza wartosc', name, ' to:', min)
    print('Najwieksza wartosc', name, ' to:', max)


def correlation_matrix(data):
    print(np.corrcoef(data))

def linear_regression(dana1,dana2,name1,name2):


    X = dana1.reshape(-1, 1)
    y = dana2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    regr = linear_model.LinearRegression()

    regr.fit(X_train,y_train)

    y_pred = regr.predict(X_test)

    plt.scatter(X_test, y_test, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.title('Wykres krzywej regresji')

    plt.show()


correlation_matrix(values.T)

dane_ilosciowe(sepal_length, 'sepal_length')

linear_regression(petal_length,petal_width,'petal_length','petal_width')