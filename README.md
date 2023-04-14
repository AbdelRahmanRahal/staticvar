# StaticVar
 A module that adds the horrors of C Static variables to Python, with Python. <br><br>

> In programming, a static variable is the one allocated “statically,” which means its lifetime is throughout the program run.

[Learn About Static Variables in C](https://www.upgrad.com/blog/static-variable-in-c) <br><br>

Python does not provide a quick native way to declare static variables. There are some *workarounds*, but they don't look very nice; so I made a module that does it for you. <br><br>

Currently, this module only supports integer, float, string and boolean types. <br><br>

#
To get started, install StaticVar by typing the following in your command line:

```
pip install StaticVar
```
<br><br>

In your project, import the StaticVar module as follows:

```python
from staticvar import Static
```
<br>

Next, declare the name of the static variable with its value and type as the arguments:

```python
# Syntax: VARIABLE_NAME = Static(VALUE, "TYPE")
foo = Static(3, "int")
```
Supported types include:
- `"int"` for integer type variables
- `"float"` for float type variables
- `"str"` for string type variables
- `"bool"` for boolean type variables

Alternatively, if no type is passed, StaticVar will infer the type.
<br><br>

To access the value of the variable, use the `get()` method:

```python
print(foo.get())
```
Output:

`> 3`<br><br>

To change the value of the variable, use the `set()` method with the desired value as the argument:

```python
# Syntax: VARIABLE_NAME.set(VALUE)
foo.set(4)
print(foo.get())
```
Output:

`> 4`<br><br>

The `set()` method also returns the new set value:

```python
print(foo.set(5))
```
Ouput:

`> 5`<br><br>

To get the type of the variable, use the `getType()` method:

```python
print(foo.getType())
```
Output:

`> int`<br><br>

Variables set using the StaticVar module are not dynamic. Trying to later assign data with different types from the originally set/inferred one will raise an error if it cannot be converted/casted:

```python
foo.set(6.9) # A float value in an integer variable type will be casted as an integer
print(foo.get())
```
Output:

`> 6`<br><br>

```python
foo.set("Hello, mum!") # Python will fail to convert this non-numerical string into integer and will raise an error
print(foo.get())
```
Output:

`> ValueError: invalid literal for int() with base 10: 'Hello, mum!'`<br><br><br>

# An example on how to utilise static variables in a simple program
Though there are better ways to do it, we can use static variables to find the factorial of a number.
```python
from staticvar import Static


# Using recursion and static variables to find the factorial of a number
def factorial(limit, reset = True):
	count = Static(1, "int")
	answer = Static(1) # If no type specified, StaticVar will infer the type

	if reset == True:
		count.set(1)
		answer.set(1)

	if count.get() <= limit:
		answer.set(answer.get() * (count.set(count.get() + 1) - 1))
		factorial(limit, False)

	return answer.get()


user_input = eval(input("Enter a number: "))
print(factorial(user_input))
```
