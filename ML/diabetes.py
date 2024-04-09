''' Using the Diabetes dataset that is in scikit-learn, answer the questions below and create a scatterplot
graph with a regression line '''

import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

print(diabetes.data.shape)

print(diabetes.DESCR)



from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    diabetes.data, diabetes.target, random_state=11
    )



mymodel = LinearRegression()
mymodel.fit(x_train, y_train)

print(mymodel.coef_)

print(mymodel.intercept_)

predicted = mymodel.predict(x_test)
expected = y_test

plt.plot(expected, predicted, ".")


x = np.linspace(0, 330, 100)
y = x

# Plotting
plt.plot(x, y)
plt.xlabel("Expceted")
plt.ylabel("Predicted")
plt.show()
 