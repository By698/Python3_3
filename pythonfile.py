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



    x = dana1.reshape(-1, 1)
    y = dana2
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    regr = linear_model.LinearRegression()

    regr.fit(x_train, y_train)

    y_pred = regr.predict(x_test)

    plt.scatter(x_test, y_test, color='black')
    plt.plot(x_test, y_pred, color='blue', linewidth=3)

    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.title('Wykres krzywej regresji')
    plt.show()


def histograms(x, y, x_name, y_name):
    fig, axs = plt.subplots(1, 2, constrained_layout=True)
    fig.patch.set_facecolor('white')
    fig.suptitle("Histogram dla dwóch najbardziej ze sobą skorelowanych cech ilościowych")
    axs[0].hist(x)
    axs[0].set_title(x_name)
    axs[1].hist(y)
    axs[1].set_title(y_name)
    plt.show()


def mapa_cieplna(x, y):
    fig, ax = plt.subplots(tight_layout=True)
    hist = ax.hist2d(x, y)
    plt.show()

dane_ilosciowe(sepal_length, 'sepal_length')

# correlation_matrix(values.T)
# histograms(petal_width, petal_length, 'petal_width', 'petal_length')
# mapa_cieplna(petal_width, petal_length)
# dane_ilosciowe(sepal_length, 'sepal_length')
# linear_regression(petal_length,petal_width)