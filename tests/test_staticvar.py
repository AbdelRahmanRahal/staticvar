import re
import sys
from io import StringIO
from typing import Callable, Dict, Optional, Union

import pytest

from staticvar import *



# ---------------------------------- Test 1 ---------------------------------- #
# Testing the basic functionality of the decorator
def test_basic_usage():
	Configure.suppress("UnpredictableBehaviourWarning")
	
	@staticvar("counter", 0)
	def my_function():
		my_function.counter += 1
		return my_function.counter

	assert my_function() == 1
	assert my_function() == 2
	assert my_function() == 3

	my_var = my_function()
	assert my_var == 4
	assert my_var == 4

	my_alias = my_function
	assert my_alias() == 5
	my_var2 = my_alias()
	assert my_var2 == 6


	@staticvar("multiply", 1)
	def multiplication_operation():
		multiplication_operation.multiply *= 2
		return multiplication_operation.multiply
	
	assert multiplication_operation() == 2
	assert multiplication_operation() == 4
	assert multiplication_operation() == 8


	@staticvar("divide", 1)
	def division_operation():
		division_operation.divide /= 2
		return division_operation.divide
	
	assert division_operation() == 0.5
	assert division_operation() == 0.25
	assert division_operation() == 0.125


	@staticvar("title", "Hello, world!")
	def my_string_function():
		my_string_function.title = " " + my_string_function.title + " "
		return my_string_function.title
	
	assert my_string_function() == " Hello, world! "
	assert my_string_function() == "  Hello, world!  "
	assert my_string_function() == "   Hello, world!   "


	@staticvar("cache", {0: 0, 1: 1}, dict)
	def fibonacci(n: int) -> int:
		if n < 0:
			raise ValueError("n must be a non-negative integer.")

		# Checking if the value has already been computated before
		if n in fibonacci.cache:
			return fibonacci.cache[n]

		fibonacci.cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
		return fibonacci.cache[n]
	
	final = fibonacci(300)
	assert fibonacci.cache[1] == 1
	assert fibonacci.cache[100] == 354224848179261915075
	assert fibonacci.cache[250] == 7896325826131730509282738943634332893686268675876375
	assert fibonacci.cache[300] == final == 222232244629420445529739893461909967206666939096499764990979600


# ---------------------------------- Test 2 ---------------------------------- #
# Testing if the decorator operates fine with maybe unusual but valid variable names
def test_valid_variable_names():
	@staticvar("counter1", 0)
	def function_with_number():
		function_with_number.counter1 += 1
		return function_with_number.counter1
	
	assert function_with_number() == 1
	assert function_with_number() == 2
	assert function_with_number() == 3


	@staticvar("c0unter", 0)
	def function_with_number_in_the_middle():
		function_with_number_in_the_middle.c0unter += 1
		return function_with_number_in_the_middle.c0unter
	
	assert function_with_number_in_the_middle() == 1
	assert function_with_number_in_the_middle() == 2
	assert function_with_number_in_the_middle() == 3


	@staticvar("_counter", 0)
	def function_with_underscore():
		function_with_underscore._counter += 1
		return function_with_underscore._counter
	
	assert function_with_underscore() == 1
	assert function_with_underscore() == 2
	assert function_with_underscore() == 3


	@staticvar("_cou__nte_r_", 0)
	def function_with_underscores():
		function_with_underscores._cou__nte_r_ += 1
		return function_with_underscores._cou__nte_r_
	
	assert function_with_underscores() == 1
	assert function_with_underscores() == 2
	assert function_with_underscores() == 3


	@staticvar("__counter__", 0)
	def function_with_dunders():
		function_with_dunders.__counter__ += 1
		return function_with_dunders.__counter__
	
	assert function_with_dunders() == 1
	assert function_with_dunders() == 2
	assert function_with_dunders() == 3


	@staticvar("__C0_UNter_3", 0)
	def function_with_mix():
		function_with_mix.__C0_UNter_3 += 1
		return function_with_mix.__C0_UNter_3
	
	assert function_with_mix() == 1
	assert function_with_mix() == 2
	assert function_with_mix() == 3


# ---------------------------------- Test 3 ---------------------------------- #
# Testing if the decorator raises an appropriate exception when an invalid variable name is provided.
def test_invalid_variable_names():
	Configure.raise_better_errors(False)
	with pytest.raises(ValueError,
					   match = ".*: variable name cannot start with a number"):
		@staticvar("1invalid_name", 0)
		def function_with_number():
			pass
	
	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar("invalid-name", 0)
		def function_with_dash():
			pass
	
	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar("invalid.name", 0)
		def function_with_fullstop():
			pass
	
	with pytest.raises(ValueError,
					   match = '.*: variable name contains an invalid character: ".*"'):
		@staticvar("invalid'name", 0)
		def function_with_single_quote():
			pass

	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar('invalid"name', 0)
		def function_with_double_quote():
			pass
	
	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar("invalid name", 0)
		def function_with_space():
			pass
	
	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar("invalid$name", 0)
		def function_with_some_symbol():
			pass

	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar("invalid\nname", 0)
		def function_with_escape_character():
			pass
	
	with pytest.raises(ValueError,
					   match = ".*: variable name contains an invalid character: '.*'"):
		@staticvar(r"invalid\nname", 0)
		def function_with_raw_string():
			pass
	
	with pytest.raises(ValueError,
					   match = ".*: variable name cannot be a reserved keyword"):
		@staticvar("def", 0)
		def function_with_reserved_keyword():
			pass


# ---------------------------------- Test 4 ---------------------------------- #
# Testing if the decorator shows the stackprinter exceptions properly when an invalid variable name is provided.
def test_stackprinter_invalid_variable_name():
	# Setting the exceptions' styles to stackprinter's
	Configure.raise_better_errors(True)
	
	# Redirecting stderr to the StringIO object
	captured_output = StringIO()
	sys.stderr = captured_output  

	with pytest.raises(SystemExit):
		@staticvar("invalid-name", 0)
		def my_function():
			pass
	
	# Resetting stderr to its original value
	sys.stderr = sys.__stderr__  

	assert re.search(
		"ValueError: .*: variable name contains an invalid character: '.*'",
		captured_output.getvalue()
	) is not None


# ---------------------------------- Test 5 ---------------------------------- #
# Testing if the decorator raises an appropriate exception when the variable name provided is not a string
def test_invalid_variable_name_type():
	# Resetting the exceptions to Python's default style
	Configure.raise_better_errors(False)

	with pytest.raises(
		TypeError,
		match = ".*: Variable name must be a string. Current type: .*"
	):
		@staticvar(["counter"], 0) # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "list[str]" cannot be assigned to parameter "var_name" of type "str" in function "staticvar"
		# 	"list[str]" is incompatible with "str"
		#
		# * This is good; because that means type checkers can tell it's wrong without needing to run the code.
		def my_function():
			pass


# ---------------------------------- Test 6 ---------------------------------- #
# Testing if the decorator shows the stackprinter exceptions properly when the variable name provided is not a string
def test_stackprinter_invalid_variable_name_type():
	# Setting the exceptions' styles to stackprinter's
	Configure.raise_better_errors(True)

	# Redirecting stderr to the StringIO object
	captured_output = StringIO()
	sys.stderr = captured_output

	with pytest.raises(SystemExit):
		@staticvar(["counter"], 0) # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "list[str]" cannot be assigned to parameter "var_name" of type "str" in function "staticvar"
		# 	"list[str]" is incompatible with "str"
		def my_function():
			pass
	
	# Resetting stderr to its original value
	sys.stderr = sys.__stderr__  

	assert re.search(
		"TypeError: .*: Variable name must be a string. Current type: .*",
		captured_output.getvalue()
	) is not None


# ---------------------------------- Test 7 ---------------------------------- #
# Testing if the decorator operates fine with different valid specified types
def test_valid_variable_type():
	# Resetting the exceptions to Python's default style
	Configure.raise_better_errors(False)

	@staticvar("counter", 0, int)
	def my_int_function():
		my_int_function.counter += 1
		return my_int_function.counter
	
	assert my_int_function() == 1
	assert my_int_function() == 2
	assert my_int_function() == 3


	@staticvar("counter", 0.2, float)
	def my_float_function():
		my_float_function.counter += 1.3
		return my_float_function.counter
	
	assert my_float_function() == 1.5
	assert my_float_function() == 2.8
	assert my_float_function() == 4.1


	@staticvar("title", "Hello, world!", str)
	def my_string_function():
		my_string_function.title = " " + my_string_function.title + " "
		return my_string_function.title
	
	assert my_string_function() == " Hello, world! "
	assert my_string_function() == "  Hello, world!  "
	assert my_string_function() == "   Hello, world!   "


	@staticvar("latin", [], list)
	def collect_the_alphabet(letter: str) -> list:
		if letter not in collect_the_alphabet.latin:
			collect_the_alphabet.latin.append(letter)
		
		return collect_the_alphabet.latin
	
	assert collect_the_alphabet('a') == ['a']
	assert collect_the_alphabet('b') == ['a', 'b']
	assert collect_the_alphabet('c') == ['a', 'b', 'c']
	

	@staticvar("counter", ("eggs", "spam"), tuple)
	def my_tuple_function():
		return my_tuple_function.counter
	
	assert my_tuple_function() == ("eggs", "spam")


	@staticvar("not_real", None, type(None))
	def imaginary():
		return imaginary.not_real
	
	assert imaginary() == None


	@staticvar("count_down", 3, Optional[int])
	def decrease_count():
		decrease_count.count_down -= 1

		if decrease_count.count_down == -1:
			decrease_count.count_down = None
			return decrease_count.count_down
		
		return decrease_count.count_down
	
	assert decrease_count() == 2
	assert decrease_count() == 1
	assert decrease_count() == 0
	assert decrease_count() == None


	@staticvar("count_up", None, Optional[int])
	def increase_count():
		if increase_count.count_up == None:
			increase_count.count_up = 0
			return increase_count.count_up
		
		increase_count.count_up += 1
		return increase_count.count_up
	
	assert increase_count() == 0
	assert increase_count() == 1
	assert increase_count() == 2


	# Technically we already know it should work because it's basically the same Optional
	@staticvar("counter", 0, Union[int, float])
	def union_function():
		union_function.counter += 1
		return union_function.counter
	
	assert union_function() == 1
	assert union_function() == 2
	assert union_function() == 3

	
	def a_callable():
		return "I am alive"
	
	# Idk why you would wanna do this, but it's properly handled so there you go
	@staticvar("state", a_callable, Callable)
	def some_other_callable():
		return some_other_callable.state()
	
	assert some_other_callable() == "I am alive"


	# This is hilarious lmao
	class DummyClass:
		def __init__(self, counter: int):
			self.counter = counter

	@staticvar("dummyObject", DummyClass(0), DummyClass)
	def dummy_function():
		dummy_function.dummyObject.counter += 1
		return dummy_function.dummyObject.counter
	
	assert dummy_function() == 1
	assert dummy_function() == 2
	assert dummy_function() == 3

# ---------------------------------- Test 8 ---------------------------------- #
# Testing if the decorator raises an appropriate warning when a complicated but valid type is passed
# (e.g. subscripted generics)
def test_complicated_types_warning():
	Configure.unsuppress('ComplicatedTypeWarning')

	with pytest.warns(ComplicatedTypeWarning):
		@staticvar("cache", {0: 0, 1: 1}, Dict[int, int])
		def fibonacci(n: int) -> int:
			if n < 0:
				raise ValueError("n must be a non-negative integer.")

			# Checking if the value has already been computated before
			if n in fibonacci.cache:
				return fibonacci.cache[n]

			fibonacci.cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
			return fibonacci.cache[n]
		
		assert fibonacci(50) == 12586269025
		assert fibonacci.cache[25] == 75025


# ---------------------------------- Test 9 ---------------------------------- #
# Testing if the decorator raises an appropriate exception when an invalid variable type is specified
def test_invalid_variable_type():
	# Resetting the exceptions to Python's default style
	Configure.raise_better_errors(False)

	with pytest.raises(
		UnsupportedTypeError,
		match = ".*: variable type must be a valid type or a generic type from the typing module. Type specified: .*"
	):
		@staticvar("counter", 0, "invalid-type") # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "Literal['invalid-type']" cannot be assigned to parameter "var_type" of type "type" in function "staticvar"
		# 	"Literal['invalid-type']" is incompatible with "type"
		def my_function():
			pass


# ---------------------------------- Test 10 --------------------------------- #
# Testing if the decorator shows the stackprinter exceptions properly when an invalid variable type is specified
def test_stackprinter_invalid_variable_type():
	# Setting the exceptions' styles to stackprinter's
	Configure.raise_better_errors(True)

	# Redirecting stderr to the StringIO object
	captured_output = StringIO()
	sys.stderr = captured_output  

	with pytest.raises(SystemExit):
		@staticvar("counter", 0, "invalid-type") # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "Literal['invalid-type']" cannot be assigned to parameter "var_type" of type "type" in function "staticvar"
		# 	"Literal['invalid-type']" is incompatible with "type"
		def my_function():
			pass
	
	# Resetting stderr to its original value
	sys.stderr = sys.__stderr__  

	assert re.search(
		"UnsupportedTypeError: .*: variable type must be a valid type or a generic type from the typing module. "
		"Type specified: .*",
		captured_output.getvalue()
	) is not None


# ---------------------------------- Test 11 --------------------------------- #
# Testing if the decorator raises an appropriate exception when the initial value and the variable type do not match.
def test_incompatible_initial_value_and_type():
	# Resetting the exceptions to Python's default style
	Configure.raise_better_errors(False)

	with pytest.raises(
		TypeError,
		match = ".*: variable must be of specified type.*. Current type: .*"
	):
		@staticvar("counter", "0", int)
		def my_function():
			pass


# ---------------------------------- Test 12 --------------------------------- #
# Testing if the decorator shows the stackprinter exceptions properly when an invalid variable type is specified
def test_stackprinter_incompatible_initial_value_and_type():
	# Setting the exceptions' styles to stackprinter's
	Configure.raise_better_errors(True)

	# Redirecting stderr to the StringIO object
	captured_output = StringIO()
	sys.stderr = captured_output  

	with pytest.raises(SystemExit):
		@staticvar("counter", "0", int)
		def my_function():
			pass
	
	# Resetting stderr to its original value
	sys.stderr = sys.__stderr__  

	assert re.search(
		"TypeError: .*: variable must be of specified type.*. Current type: .* ",
		captured_output.getvalue()
	) is not None


# ---------------------------------- Test 13 ---------------------------------- #
# Testing if the decorator raises an appropriate when the decorated function is a method in a class and there are multiple instances of the class.
def test_unpredictable_behaviour_warning():
	Configure.unsuppress("UnpredictableBehaviourWarning")

	with pytest.warns(UnpredictableBehaviourWarning):
		class AnInnocentClass:
			@staticvar("anInnocentVariable", 0)
			def my_method(self):
				pass
	
	with pytest.warns(UnpredictableBehaviourWarning):
		@staticvar("count", 0)
		def my_function():
			pass