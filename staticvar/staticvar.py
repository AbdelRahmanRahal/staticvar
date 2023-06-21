from typing import Any, Callable
from functools import wraps

def staticvar(var_name: str, initial_value: Any, var_type: type = Any):
	'''

	Decorator to create a static variable for the target function.

	Args:
		var_name (str): static variable name.
		initial_value (Any): initial value for the variable.
		var_type (type): type of the variable. Leave empty to make it dynamic.

	Returns:
		Callable: the decorated function.

	Raises:
		TypeError: if a type is specified and it does not match the initial value.
		ValueError: if the variable name does not follow Python's syntax rules.
	
	'''
	
	def decorator(func):
		# Checking if the initial value matches the type specified.
		if var_type != Any and not isinstance(initial_value, var_type):
			raise TypeError(f"{func.__name__}.{var_name} must be of type {var_type}. Current type: {initial_value.__class__}")
		
		# Checking if the variable name does not follow Python's syntax rules.
		if var_name[0].isdecimal():
			raise ValueError(f"variable name {func.__name__}.{var_name} cannot start with a number")
		
		for ch in var_name:
			if not (ch == "_" or ch.isalpha() or ch.isdecimal()):
				raise ValueError(f"variable name {func.__name__}.{var_name} has an invalid character: '{ch}'")

		setattr(func, var_name, initial_value)
		
		
		return func
	return decorator
