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

> **Warning**: staticvar only supports Python 3.10 and higher.


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

Use the static variable by preceding it with the name of the function its used in:

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
	if bar.spam is True:
		return bar.eggs
```
<br />

### Typing
staticvar supports typing!... kind of... You can insert the type of the static variable as an argument in the decorator to ensure that the initial value is of the expected type, but staticvar cannot guarantee later values to be of the same type.

Here's how you can type-check your static variable with staticvar:

```python
# Syntax: @staticvar("VARIABLE_NAME", INITIAL_VALUE, VARIABLE_TYPE)
@staticvar("foo", 0, int)
def bar():
	pass
```
> **Note**: staticvar supports most types from Python's built-in `typing` module, but it cannot force type checking on
complicated types. See [edge cases](https://github.com/AbdelRahmanRahal/staticvar/blob/main/README.md#complicated-types).

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


# Configure
staticvar provides a class for editing its configurations. 
### Importing
To get started, import `Configure` into your project:
```python
from staticvar import Configure
```
<br />

### Suppressing and Unsuppressing Warnings
staticvar raises various warnings when possibly misused. If you know what you're doing though, you can suppress these warnings using the `.suppress()` method, as well as unsuppress them later using `.unsuppress()`.

Here is the current list of warnings used by staticvar:
- `ComplicatedTypeWarning`
- `UnpredictableBehaviourWarning`

Just add the name of the warning you want to suppress as a string (you can write more than 1 in one go):
```python
Configure.suppress('ComplicatedTypeWarning')
```
<br />

### Better Errors
staticvar uses the `stackprinter` module to print more readable errors. Unfortunately, with how it's set up, all the
errors raised with it are SystemExit errors. They are not caught by the convential `Exception` class. You can either
catch `BaseException` or `SystemExit` or just disable this feature entirely to fallback to normal python exceptions.

You can write the following at the top of your file to raise the actual exceptions (and print the normal python traceback):
```python
Configure.raise_better_errors(False)
```
<br />

> **Note**: staticvar has some custom exceptions (e.g. UnsupportedTypeError). They can be imported and caught.

# Edge Cases
### Scope
staticvar doesn't create static variables **exactly** like the ones in C and C++, as that cannot be made with just Python.
Instead, it assigns the variable name you specify to the target function as an attribute of it. This means that its scope
is not within the function its defined in like C, but rather the scope of the function itself.

Take a look at this function to understand more (you don't need to focus on the details of it):
```python
@staticvar("calls", 0)
def reverse_integer(n: int) -> int:
	reverse_interger.calls += 1 # Incrementing the number of times reverse_integer() is called

	sign = 1 if n >= 0 else -1 # Preserving the sign of the number
	n = abs(n) # Working with the absolute value of n

	reversed_number: int = 0
	while n != 0:
		n, digit = divmod(n, 10) # Getting the last digit and the rest of n
		reversed_number = reversed_number * 10 + digit 
	
	return sign * reversed_number
```
<br />

If we call this function, say, twice, then try to access the value of `reverse_interger.calls`, it will actually retrun 2:
```python
print(reverse_integer(123)) # Output: 321
print(reverse_integer(2468)) # Output: 2468

print(reverse_interger.calls) # Output: 2, this would raise an error in C
```

Therefore, you don't need to put the static variable in the return of the function if you don't want to.


### Lifetime
Similarly, the lifetime for staticvar variables is not always till the end of the program like in C. This is because of Python's support for nesting function definitions. The lifetime of the variable is actually just the lifetime of the function its declared in.

The following code should clear this up a little:
```python
def main_function():
	@staticvar("count", 0, int)
	def nested_function():
		nested_function.count += 1
		return nested_function.count
	
	print(nested_function(), end=" ")
	print(nested_function(), end=" ")
	print(nested_function())

main_function()
'''
Output:
1 2 3
'''

main_function() # The nested function will then be redeclared, thus resetting the counter
'''
Output:
1 2 3

NOT 4 5 6
'''
```
<br />

staticvar provides a warning if used on nested functions since they basically defeat the purpose of using the static variable.
If you know what you're doing, you can just do `from staticvar import Configure` and suppress the warning by writing this line at the top of your code:
```python
Configure.suppress("UnpredictableBehaviourWarning")
```

### "Complicated" Types
Most generic types like `TypeVar` or `ParamSpec`, detailed/parameterized generics like `dict[str, int]`, and some other types
don't work with staticvar. This is because staticvar does not assign the type specified to the static variable; it checks if
it matches the the type of the initial value of it. With current Python's capibilities (and maybe mine, too), it's hard to
account for each type without sacrificing some of the efficiency.

The following code:
```python
T = TypeVar("T")
@staticvar("count", 0, T)
def my_function():
	pass

my_function()
```

should raise this error:
```
> UnsupportedTypeError: my_function.count: variable type must be a valid type or a generic type from the typing module. Type specified: ~T
```