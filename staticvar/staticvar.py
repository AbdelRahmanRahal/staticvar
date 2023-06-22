from inspect import isclass
from keyword import iskeyword
from typing import Any, get_args, get_origin


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
		# Checking if the variable name is not a string
		if type(var_name) != str:
			raise ValueError(f"{func.__name__}: Variable name must be a string. Current type: {(type(var_name))}")
		
		full_name = f"{func.__name__}.{var_name.encode('unicode_escape').decode()}"

		# Checking if the type specified is not a valid type or a generic type from the typing module
		var_origin = get_origin(var_type)
		var_args = get_args(var_type)

		if not (isclass(var_type) or
				(var_origin is not None and isinstance(var_origin, type)) or
				(var_args is not None and len(var_args) > 0)):
			raise ValueError(f"{full_name}: "
							 f"variable type must be a valid type or a generic type from the typing module. "
							 f"Type specified: {var_type}")
		
		# Checking if the initial value does not match the type specified.
		if var_type != Any and not isinstance(initial_value, var_type):
			raise TypeError(f"{full_name}: variable must be of type {var_type}. Current type: {type(initial_value)}")
		
		# Checking if the variable name does not follow Python's syntax rules.
		if iskeyword(var_name):
			raise ValueError(f"{full_name}: variable name cannot be a reserved keyword")
		
		if var_name[0].isdecimal():
			raise ValueError(f"{full_name}: variable name cannot start with a number")
		
		for ch in var_name:
			if not (ch == "_" or ch.isalpha() or ch.isdecimal()):
				raise ValueError(f"{full_name}: variable name contains an invalid character: {repr(ch)}")
		
		setattr(func, var_name, initial_value)
		
		return func
	return decorator
