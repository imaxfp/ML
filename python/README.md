### HOWTO Python.

 
#### Methods vs Functions 

#### Method: 

1. Method is called by its name, but it is associated to an object (dependent).
2. A method is implicitly passed the object on which it is invoked.
3. It may or may not return any data.
4. A method can operate on the data (instance variables) that is contained by the corresponding class.

##### Python 3 User-Defined Method
```python
class ABC : 
	def method_abc (self): 
		print("I am in method_abc of ABC class. ") 

class_ref = ABC() # object of ABC class 
class_ref.method_abc() 
``` 

##### Python 3 Inbuilt method 
```python
import math 

ceil_val = math.ceil(15.25) 
print( "Ceiling value of 15.25 is : ", ceil_val) 
```


#### Function

The function can or can not return one or more values, 3 types of functions:

Types:
1. Built-in functions, such as print() - https://docs.python.org/3/library/functions.html
2. User-Defined Functions (UDFs), which are functions that users create to help them out
3. Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.

Parameters:
1. Function is block of code that is also called by its name. (independent)
2. The function can have different parameters or may not have any at all. If any data (parameters) are passed, they are passed explicitly.
3. It may or may not return any data.
4. Function does not deal with Class and its instance concept.

##### Basic Function Structure:
```python
def function_name ( arg1, arg2, ...) :  
	# function body 
	
```

##### Python 3 User-Defined Function :
```python
def Subtract (a, b): 
	return (a-b) 

print( Subtract(10, 12) ) # prints -2 

print( Subtract(15, 6) ) # prints 9 
```

##### Python 3 Inbuilt Function :
```python
s = sum([5, 15, 2]) 
print( s ) # prints 22 

mx = max(15, 6) 
print( mx ) # prints 15 
```

##### Difference between method and function
1. Simply, function and method both look similar as they perform in almost similar way,
but the key difference is the concept of ‘Class and its Object‘.

2. Functions can be called only by its name, as it is defined independently. 
But methods can’t be called by its name only, we need to invoke the class by a reference of that class in which it is defined,
i.e. method is defined within a class and hence they are dependent on that class.


##### Parameters vs Arguments

The first argument of every class method is always a reference to the current instance of the class, which in this case is Summation.
By convention, this argument is called self.


##### self
```html
http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html
```


##### Docs
```html
https://www.datacamp.com/community/tutorials/functions-python-tutorial?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=1t1&utm_creative=332602034358&utm_targetid=dsa-473406571355&utm_loc_interest_ms=&utm_loc_physical_ms=9061015&gclid=Cj0KCQjw-tXlBRDWARIsAGYQAmeVXpPLxAB7FQOagSY51fAmGol2hUOVKuFZs4AVCxEX9P-lBO5lclMaAjp_EALw_wcB
```
 