class StaticInt():
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