import os
import sys
import threading
from types import TracebackType
from typing import Optional, Type

import stackprinter

from .exceptions import *


class Configure():
	'''
	Class to manage staticvar's configurations.
	'''
	
	# The reason they are in a dict instead of just making a method for each one is to support adding more warnings
	__suppress: dict[str, bool] = {
		"UnpredictableBehaviourWarning": False,
		"ComplicatedTypeWarning": False
	}

	__raise_better_errors: bool = True


	def __new__(cls, *args, **kwargs) -> None:
		'''
		Raises an error if the user tries to create an object
		out of `Configure()`; it should only be used as itself.
		'''
		with StaticvarExceptionHandler():
			raise IllegalInstantiationError("Configure() class should not be instantiated as an object")
	
	
	@staticmethod
	def suppress(*args: str) -> None:
		'''
		Suppresses warnings passed

		Args:
			*args (str): the warning names to suppress (can accept more than 1).
		
		Raises:
			LookupError: if one of the warnings passed is not found in __raise_better_errors.
			TypeError: if an argument of any type but string is passed.
		'''
		for warning in args:
			if warning not in Configure.__suppress:
				with StaticvarExceptionHandler():
					raise LookupError(f"Warning {warning} not found in warnings list.")
			
			if not isinstance(warning, str):
				with StaticvarExceptionHandler():
					raise TypeError(f"Configure.suppress() only takes string arguments. Current type: {type(warning)}")

			Configure.__suppress[warning] = True
	

	@staticmethod
	def unsuppress(*args: str) -> None:
		'''
		Unsuppresses warnings passed

		Args:
			*args (str): the warning names to unsuppress (can accept more than 1).
		
		Raises:
			LookupError: if one of the warnings passed is not found in __raise_better_errors.
			TypeError: if an argument of any type but string is passed.
		'''
		for warning in args:
			if warning not in Configure.__suppress:
				with StaticvarExceptionHandler():
					raise LookupError(f"Warning {warning} not found in warnings list.")
			
			if not isinstance(warning, str):
				with StaticvarExceptionHandler():
					raise TypeError(f"Configure.suppress() only takes string arguments. Current type: {type(warning)}")

			Configure.__suppress[warning] = False
	

	@staticmethod
	def suppressed() -> dict[str, bool]:
		'''
		Returns a dictionary of the warnings and whether they're suppressed or not.
		'''
		return Configure.__suppress.copy()
	

	@staticmethod
	def raise_better_errors(value: Optional[bool] = None) -> Optional[bool]:
		'''
		Sets whether to raise staticvar's exceptions in Python's default style or staticvar's
		style (powered by [stackprinter](https://github.com/cknd/stackprinter) <3).
		If no value is provided, it returns the current setting.
		
		Args:
			value (Optional[bool]): set to `True` for staticvar's style and `False` to fall back to python's default style. Leave empty to get the current setting.
		
		Returns:
			bool: whether to raise staticvar's exceptions in Python's default style or staticvar's style.
		
		Raises:
			TypeError: if an argument of any type but boolean or None is passed.
		'''
		if value is None:
			return Configure.__raise_better_errors
		
		if not isinstance(value, bool):
			with StaticvarExceptionHandler():
				raise TypeError(
					f"Configure.raise_better_errors() only takes boolean arguments. Current type: {type(value)}"
				)
		
		Configure.__raise_better_errors = value
	

class StaticvarExceptionHandler():
	def __init__(self) -> None:
		'''
		Exception traceback context manager class.

		This class is intended to be used with `with` statements.
		It handles the staticvar custom exceptions and logs a
		much prettier exception traceback than the default one.

		To fall back to Python's default staticvar exceptions, use `Configure.raise_better_errors(False)`.
		'''
		self.lock = threading.Lock()
	

	def __enter__(self) -> None:
		self.lock.acquire()
	

	def __exit__(
			self,
			exc_type: Optional[Type[BaseException]],
			exc_value: Optional[BaseException],
			exc_traceback: Optional[TracebackType]
		) -> Optional[bool]:
		# Checking an error is raised and that __raise_better_errors is True
		if exc_type is not None and Configure.raise_better_errors():
			# Getting the directory of the current file to suppress it
			full_path = os.path.abspath(__file__)
			directory = os.path.dirname(full_path).replace('\\', '/')
			
			# Logging the exception details to the error stream
			stackprinter.show(
				sys._getframe(2),
				suppressed_paths = [directory],
				style = 'darkbg2'
			)
			# Logging the main error message to the error stream
			print(f"\033[91m{exc_type.__name__}: {exc_value}\033[0m", file = sys.stderr)

			# Terminating the program
			sys.exit(1)
		
		self.lock.release()
		return False # Re-raising the exception if it occurs