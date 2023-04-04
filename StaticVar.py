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


		
class StaticInt():
	__value = None
	def __init__(self, IntValue = 0):
		if str(type(IntValue)) != "<class 'int'>":
			try:
				self.__value = int(IntValue)

			except ValueError as VE:
				raise VE
		else:
			self.__value = IntValue

	def set(self, IntValue):
		if str(type(IntValue)) != "<class 'int'>":
			try:
				self.__value = int(IntValue)
			except ValueError as VE:
				raise VE

		else:
			self.__value = IntValue

		return self.__value

	def value(self):
		return self.__value


class StaticFloat():
	def __init__(self, FloatValue = 0):
		if str(type(FloatValue)) != "<class 'float'>":
			try:
				self.__value = float(FloatValue)

			except ValueError as VE:
				raise VE
		else:
			self.__value = FloatValue

	def set(self, FloatValue):
		if str(type(FloatValue)) != "<class 'int'>":
			try:
				self.__value = float(FloatValue)
			except ValueError as VE:
				raise VE

		else:
			self.__value = FloatValue

		return self.__value

	def value(self):
		return self.__value


class StaticStr():
	def __init__(self, StringValue = ""):
		if str(type(StringValue)) != "<class 'str'>":
			try:
				self.__value = str(StringValue)

			except ValueError as VE:
				raise VE
		else:
			self.__value = StringValue

	def set(self, StringValue):
		if str(type(StringValue)) != "<class 'str'>":
			try:
				self.__value = str(StringValue)
			except ValueError as VE:
				raise VE

		else:
			self.__value = StringValue

		return self.__value

	def value(self):
		return self.__value