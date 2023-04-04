class InvalidTypeError(Exception):
	def __init__(self, vtype):
		self.type = vtype
		super().__init__(f"Unsupported data type entered: {self.type}")