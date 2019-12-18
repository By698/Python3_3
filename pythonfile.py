import numpy as np

data = np.loadtxt('iris.data')
#
# 1. sepal length in cm
#    2. sepal width in cm
#    3. petal length in cm
#    4. petal width in cm
#    5. class:
sepal_length, sepal_width, petal_length, petal_width, iris_class = data.T
