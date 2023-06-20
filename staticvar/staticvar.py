from typing import Any, Callable
from functools import wraps

def staticvar(var_name: str, initial_value: Any, var_type: type = Any) -> Callable:
	'''
	Decorator to create a static variable for the given function

	Args:
		var_name (str): static variable name.
		initial_value (Any): initial value for the variable.
		var_type (type): type of the variable. Leave empty to make it dynamic.

	Returns:
		Callable: the decorated function.

	Raises:
		TypeError: if a type is specified and it does not match the initial value.
	'''
	
	def decorator(func):
		if var_type != Any and not isinstance(initial_value, var_type):
			raise TypeError(f"{func.__name__}.{var_name} must be of type {var_type}. Current type: {initial_value.__class__}")
		
		setattr(func, var_name, initial_value)
		
		@wraps(func)
		def wrapper(*args, **kwargs):
			return func(*args, **kwargs)
		
		return wrapper
	return decorator
