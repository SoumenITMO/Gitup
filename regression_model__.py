__author__ = 'Soumen'

from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from pylab import plot, title, show , legend
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib as plt
import pandas
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model


"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
# Load the diabetes dataset
diabetes = datasets.load_diabetes()
# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
# Create linear regression object
regr = linear_model.LogisticRegression()
# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
"""

data = pandas.read_csv("D3-data-file-refugee.csv", delimiter='\t')

#Linear regression example
# This is a very simple example of using two scipy tools
# for linear regression, polyfit and stats.linregress
#Sample data creation
#number of points
n = 10
t = linspace(-18, 18, n)
#parameters
#a = 8; b = 2
a = 31
b = 76
x = polyval(data['Lebanon'], t)
#add some noise
xn = x
#Linear regressison -polyfit - polyfit can be used other orders polys
(ar, br) = polyfit(t, xn, 1)
xr = polyval([ar, br], t)
#compute the mean square error
err = sqrt(sum((xr-xn)**2)/n)
print('Linear regression using polyfit')
#print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, ms error= %.3f' % (a, b, ar, br, err))
#matplotlib ploting
title('Linear Regression Example')
plot(t, x, 'y.--')
plot(t, xn, 'k.')
plot(t, xr, 'r.-')
legend(['original', 'plus noise', 'regression'])
show()
#Linear regression using stats.linregress
(a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
print('Linear regression using stats.linregress')
print('parameters: a=%.2f b=%.2f \nregression: a=%.2f b=%.2f, std error= %.3f' % (a, b, a_s, b_s, stderr))
