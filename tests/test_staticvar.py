from staticvar import staticvar

def test_basic_usage():
	@staticvar("counter", 0)
	def my_function():
		my_function.counter += 1
		return my_function.counter

	assert my_function() == 1
	assert my_function() == 2
	assert my_function() == 3

# ---------------------------------- Test 1 ---------------------------------- #
# Test with an invalid variable name:
# Test if the decorator raises an appropriate exception when an invalid variable name is provided.

def test_invalid_variable_name():
	try:
		@staticvar("invalid-name", 0)
		def my_function():
			pass
	except ValueError:
		pass
	else:
		assert False, "Expected a ValueError with an invalid variable name."

# ---------------------------------- Test 2 ---------------------------------- #
# Test with an invalid VARIABLE_TYPE:
# Test if the decorator raises an appropriate exception when an invalid VARIABLE_TYPE is provided.

def test_invalid_variable_type():
	try:
		@staticvar("counter", 0, "invalid-type")
		def my_function():
			pass
	except ValueError:
		pass
	else:
		assert False, "Expected a ValueError with an invalid variable type."

# # ---------------------------------- Test 3 ---------------------------------- #
# # Test with an incompatible initial value and VARIABLE_TYPE:
# # Test if the decorator raises an appropriate exception when the initial value and the VARIABLE_TYPE do not match.

# def test_incompatible_initial_value_and_type():
# 	try:
# 		@staticvar("counter", "0", int)
# 		def my_function():
# 			pass
# 	except TypeError:
# 		pass
# 	else:
# 		assert False, "Expected a TypeError with an incompatible initial value and type."

# # ---------------------------------- Test 4 ---------------------------------- #
# # Test with multiple instances of a class:
# # Test if the static variable behaves correctly when the decorated function is a method in a class and there are multiple instances of the class.

# class MyClass:
# 	@staticvar("counter", 0)
# 	def my_method(self):
# 		self.my_method.counter += 1
# 		return self.my_method.counter

# def test_multiple_class_instances():
# 	instance1 = MyClass()
# 	instance2 = MyClass()

# 	assert instance1.my_method() == 1
# 	assert instance1.my_method() == 2
# 	assert instance2.my_method() == 3
# 	assert instance2.my_method() == 4
