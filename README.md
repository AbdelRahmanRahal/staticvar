# StaticVar
 A module that adds static variables to Python. <br><br>

> In programming, a static variable is the one allocated “statically,” which means its lifetime is throughout the program run.

[Learn About Static Variable in C](https://www.upgrad.com/blog/static-variable-in-c) <br><br>

Python does not provide a quick native way to declare static variables. There are some *workarounds*, but they don't look very nice; so I made a module that does it for you. <br><br>

Currently, this module only supports integer, float and string types as `StaticInt`, `StaticFloat`, and `StaticString` respectively. <br><br>

#
To get started, import the needed class(es):

```python
from StaticVar import StaticInt
```
<br>

Next, declare the name of the static variable and its value:

```python
foo = StaticInt(3)
```
If no value is provided, it defaults to 0. (Just like a certain peculiar programming language...) <br><br>

To access the value of the variable, use the `value()` method:

```python
print(foo.value())
```
Output:

`> 3`<br><br>

To change the value of the variable, use the `set()` method:

```python
foo.set(4)
print(foo.value)
```
Output:

`> 4`<br><br>

Alternatively, you can just redefine the variable object with the new value:

```python
foo = StaticInt(5)
print(foo.value)
```
Ouput:

`> 5`<br><br>

Variables set using the StaticVar module are not dynamic. Trying to later assign data with different types from the originally set one will raise an error if it cannot be converted/casted:

```python
foo.set(6.9) #A float value in an integer variable type will be casted as an integer
print(foo.value())
```
Output:

`> 6`<br><br>

```python
foo.set("Hello, mum!")
print(foo.value())
```
Output:

`> ValueError: invalid literal for int() with base 10: 'Hello, mum!'`<br><br><br>

# An example on how to utilise static variables
I'll do it in the morning, I'm really exhausted.
