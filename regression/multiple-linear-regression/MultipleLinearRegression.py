# Multiple Linear regression
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
print("initial dataset:")
print(dataset)
# X is independent variables - "R&D, Administration, Marketing, etc"
X = dataset.iloc[:, :-1].values
# y is dependent variable - "Profit"
y = dataset.iloc[:, 4].values


def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    return regressor_OLS


# Encoding the Independent Variable.
# Encoding categorical data "California, New York, Florida, etc" to dummy variables.
# Instead of states will get 3 columns.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding dummy variable trap DVT
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

print(type(X_train))

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Create vector of prediction
y_pred = regressor.predict(X_test)

print("y_test:")
for i in range(len(y_test)):
    print(y_test[i])

print("y_pred:")
for i in range(len(y_pred)):
    print(y_pred[i])

# Building the optimal model using Backlward Elimination
import statsmodels.formula.api as sm

newArrayType = np.ones((50, 1)).astype(int)
X = np.append(arr=newArrayType, values=X, axis=1)
# Initialize original matrix of features of independent variables.
X_opt = X[:, [0, 1, 2, 3, 4, 5]]

# STEP 2 - Fit the full model with all posible predictors - (value of two or more idependent variables)
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()

# STEP 3 - Consider the predictor with the higest P-value. If P > SL "significant level", to to the STEP 4.
# Otherwise your model is ready.

# const, x1, x2 - dummy variables for State.
# x3 - R&D Spend
# x4 - Administration
# x5 - Marketing Spend
print(regressor_OLS.summary())

# STEP 4 Can be done manually Remove the predictor - Removed dummy variable with highest P-value "x2 - 0.990"
# X = np.append(arr=newArrayType, values=X, axis=1)
# X_opt = X[:, [0, 1, 3, 4, 5]]
# print(regressor_OLS.summary())


SL = 0.07
regressor_OLS = backwardElimination(X_opt, SL)
print(regressor_OLS.summary())
