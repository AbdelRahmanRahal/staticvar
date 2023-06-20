# staticvar
A decorator that adds the horrors of C Static variables to Python, with Python.<br /><br />

> In programming, a static variable is the one allocated “statically,” which means its lifetime is throughout the program run.

[Learn About Static Variables in C](https://www.upgrad.com/blog/static-variable-in-c)
<br /><br />

Check out the changelog for staticvar [here](https://github.com/AbdelRahmanRahal/staticvar/blob/main/CHANGELOG.md).
<br /><br />

# Installation
To get started, install staticvar by typing the following in your command line:

```
pip install staticvar
```
<br />

You can also manually download and install staticvar from [PyPI](https://pypi.org/project/staticvar/).<br><br>

> **Warning**: staticvar only supports Python 3.5 and higher.


# Usage
### Importing
In your project, import the staticvar decorator as follows:

```python
from staticvar import staticvar
```
<br />

### Basics
Next, use the staticvar decorator above the target function and declare the name of the static variable along with its initial value as follows:

```python
# Syntax: @staticvar("VARIABLE_NAME", INITIAL_VALUE)
@staticvar("foo", 0)
def bar():
	pass
```
<br />

You use the static variable by preceding it with the name of the function its used in:

```python
@staticvar("foo", 0)
def bar():
	# Syntax: FUNCTION.VARIABLE_NAME
	bar.foo += 1
```
<br />

You can declare more than 1 static variable by stacking staticvar decorators at the top of the target function, and you can use all sorts of different data types:

```python
@staticvar("eggs", 2.71828183)
@staticvar("spam", True)
def bar():
    if bar.spam == True:
        return bar.eggs
```
<br />

### Typing
staticvar supports typing!... kind of... You can insert the type of the static variable as an argument in the decorator to ensure that the initial value is of the expected type, but staticvar cannot guarantee later values to be of the same type.

Here's how you can type-annotate your static variable with staticvar:

```python
# Syntax: @staticvar("VARIABLE_NAME", INITIAL_VALUE, VARIABLE_TYPE)
@staticvar("foo", 0, int)
def bar():
	pass
```
> **Note**: staticvar supports types from the Python built-in `typing` module.

<br />

If a variable of an unexpected type is passed, staticvar will raise a TypeError and terminate the program:

```python
initialiser = 0.01

@staticvar("count", initialiser, int)
def bar():
	bar.count += 1
```
Output:

`> TypeError: bar.count must be of type <class 'int'>. Current type: <class 'float'>`
<br /><br />

# An example on how to utilise staticvar and static variables in a simple program
This is better done with Python's `@cache` decorator from `functools`, but staticvar can be used for memoization.

Here, we use staticvar to quickly print out the values of the Fibonacci sequence from 0 to 500. Normally, this program would take incredibly long to finish, but with staticvar, it will finish it in less than a second.

```python
from staticvar import staticvar

@staticvar("cache", {0: 0, 1: 1}, dict)
def fibonacci(n: int) -> int:
	if n < 0:
		raise ValueError("n must be a non-negative integer.")

	# Checking if the value has already been computated before
	if n in fibonacci.cache:
		return fibonacci.cache[n]

	fibonacci.cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
	return fibonacci.cache[n]

for i in range(0, 501):
	print(fibonacci(i))
```
Console:

![After the program runs, the values of the Fibonacci sequence from 0 to 500 get printed out instantaneously.](https://github.com/AbdelRahmanRahal/staticvar/blob/main/exampleconsole.gif?raw=true)
