from Errors import *

class Static():
	__value = None
	def __init__(self, value, vtype = "any"):
		if "__value" not in self.__dict__:
			if vtype == "any":
				self.__value = value
				match str(type(value)):
					case "<class 'int'>":
						self.__type = "int"
					case "<class 'float'>":
						self.__type = "float"
					case "<class 'str'>":
						self.__type = "str"
					case "<class 'bool'>":
						self.__type = "bool"
					case _:
						raise InvalidTypeError(type(value))
			else:
				self.__type = vtype
				match self.__type:
					case "int":
						try:
							self.__value = int(value)

						except ValueError as VE:
							raise VE
					case "float":
						try:
							self.__value = float(value)

						except ValueError as VE:
							raise VE
					case "str":
						try:
							self.__value = str(value)

						except ValueError as VE:
							raise VE
					case "bool":
						try:
							self.__value = bool(value)

						except ValueError as VE:
							raise VE
					case _:
						raise InvalidTypeError(f"\"{vtype}\"")

	def set(self, value):
		match self.__type:
				case "int":
					try:
						self.__value = int(value)

					except ValueError as VE:
						raise VE
				case "float":
					try:
						self.__value = float(value)

					except ValueError as VE:
						raise VE
				case "str":
					try:
						self.__value = str(value)

					except ValueError as VE:
						raise VE
				case "bool":
					try:
						self.__value = bool(value)

					except ValueError as VE:
						raise VE

		return self.__value

	def get(self):
		return self.__value
