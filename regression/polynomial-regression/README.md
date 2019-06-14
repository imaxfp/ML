### Polynomial regression demo

![Example.png](../../img/polynomial-regression/example.png) 

Main formula

```text
y - dependent 
β0 - starting point
β1 - slope
x - independent
```
![MainFormula.png](../../img/polynomial-regression/MainFormula.png)


Analyze data set with simple linear regression 
![LinearExample.png](../../img/polynomial-regression/LinearExample.png)
As you can see the prediction is not accurate as well


```python
poly_reg = PolynomialFeatures(degree=2)
```
This is why for growing data by exponent will be better to use polynomial regression. 
![LinearExample.png](../../img/polynomial-regression/PolynomialRegression.png)


With specific degree customization, we can manage our prediction line
```python
poly_reg = PolynomialFeatures(degree=30)
```

![LinearExample.png](../../img/polynomial-regression/Degree.png)

### Why is it steel linear ?
 
