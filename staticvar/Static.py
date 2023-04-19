from varname import varname

StaticVars = dict()

class Static():
	def __init__(self, value, vtype = "infer"):
		self.__name = varname()

		if self.__name not in StaticVars:
			if vtype == "infer":
				self.__value = value
				if str(type(value).__name__) in ("int", "float", "str", "bool"):
					self.__type = str(type(value).__name__)
				else:
					raise InvalidTypeError(str(type(value).__name__))
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

			StaticVars[self.__name] = (self.__value, self.__type)

		else:
			self.__value = StaticVars[self.__name][0]
			self.__type = StaticVars[self.__name][1]


	def set(self, value):
		match StaticVars[self.__name][1]:
			case "int":
				try:
					StaticVars[self.__name] = (int(value), "int")

				except ValueError as VE:
					raise VE
			case "float":
				try:
						StaticVars[self.__name] = (float(value), "float")

				except ValueError as VE:
					raise VE
			case "str":
				try:
					StaticVars[self.__name] = (str(value), "str")

				except ValueError as VE:
					raise VE
			case "bool":
				try:
					StaticVars[self.__name] = (bool(value), "bool")

				except ValueError as VE:
					raise VE

		self.__value = StaticVars[self.__name][0]

		return self.__value


	def get(self):
		return StaticVars[self.__name][0]

	# ————— getValue as an alias of get —————
	getValue = get

	def getType(self):
		return StaticVars[self.__name][1]


class InvalidTypeError(Exception):
	def __init__(self, vtype):
		super().__init__(f"Unsupported data type entered: {vtype}")


class UnsupportedMethodError(Exception):
	def __init__(self):
		super().__init__("")