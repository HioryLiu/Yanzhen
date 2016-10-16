import numpy as np
from numpy import *
import matplotlib.pyplot as plt

dataSet = [[1,2],[2,3],[3,4]]

dataMat = mat(dataSet).T
plt.scatter(dataMat[0], dataMat[1], c='red', marker='o')

X = np.linspace(-2,2,100)

Y = 2.8*X+9
plt.plot(X,Y)
plt.show()