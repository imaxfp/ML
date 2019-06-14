# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting linear regression just for comparison
from sklearn.linear_model import LinearRegression

lin_regressor = LinearRegression()
lin_regressor.fit(x, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=2)
x_poly = poly_reg.fit_transform(x)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

# Visualising the Linear Regression
plt.scatter(x, y, color='red')
plt.plot(x, lin_regressor.predict(x), color='blue')
plt.title('Linear regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression
plt.scatter(x, y, color='red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

position_level = 10
print("predicted salary with linear regression for position level - ", position_level)
print(lin_regressor.predict([[position_level]]))


print("predicted salary with polynomial regression for position level - ", position_level)
print(lin_reg_2.predict(poly_reg.fit_transform([[position_level]])))
