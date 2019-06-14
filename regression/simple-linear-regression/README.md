### Simple linear regression demo

Simple Linear Regression where salary is predicted only on years of experience.
One independent variable.


Simple linear regression gets its adjective "simple" because it concerns the study of only one predictor variable.

Predictive modelling technique which investigates the relationship between a dependent (target) and independent variable (s) (predictor).
This technique is used for forecasting, time series modelling and finding the causal effect relationship between the variables.
For example, relationship between rash driving and number of road accidents by a driver is best studied through regression.

Linear regression models are used to show or predict the relationship between two variables or factors. 
The factor that is being predicted (the factor that the equation solves for) is called the dependent variable.
The factors that are used to predict the value of the dependent variable are called the independent variables.

Using this insight, we can predict future sales of the company based on current & past information.

Training Dataset: The sample of data used to fit the model.
Test Dataset: The sample of data used to provide an unbiased evaluation of a final model fit on the training dataset.

![MinimizeErrors.jpg](../../img/simple-linear-regression/MinimizeErrors.jpg)


```text
The simple linear regression model is represented like this: y = β0 +β1 + X

The equation that describes how y is related to x is known as the regression model. 

``` 



![MainFormula.jpg](../../img/simple-linear-regression/Y=b0+b1X.jpg)



### How to calculate linear regression using least square method
```text


First, find the 'mean' of X and Y lines
   
_    X1 + X2 + Xn
X = -------------
          n
```
![MainFormula.jpg](../../img/simple-linear-regression/Mean.jpg)



```text
Find the observation distance to the X and Y 'mean'
```
![MainFormula.jpg](../img//simple-linear-regression/ObservationDistance.jpg)


```text
y = β0 + β1 + X Determination what is β0 and β1 
```
![Slope.jpg](../../img/simple-linear-regression/Slope.jpg)


```text
Salary example:

y(salary) - dependent 
β0 - starting point
β1 - slope
x(experience) - independent

```
![SalaryExample.jpg](../../img/simple-linear-regression/SalaryExample.jpg)





links:
```html

https://newonlinecourses.science.psu.edu/stat501/node/251/
https://www.thebalancesmb.com/what-is-simple-linear-regression-2296697
https://www.youtube.com/watch?v=JvS2triCgOYhttps://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/
https://towardsdatascience.com/overfitting-vs-underfitting-a-complete-example-d05dd7e19765

```


