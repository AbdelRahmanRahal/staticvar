import pytest

from staticvar import *


# ---------------------------------- Test 1 ---------------------------------- #
def test_suppress():
	Configure.suppress('ComplicatedTypeWarning', 'UnpredictableBehaviourWarning')
	
	assert Configure.suppressed() == {
		"ComplicatedTypeWarning": True,
		"UnpredictableBehaviourWarning": True
	}


	Configure.unsuppress('UnpredictableBehaviourWarning')

	assert Configure.suppressed() == {
		"ComplicatedTypeWarning": True,
		"UnpredictableBehaviourWarning": False
	}


	Configure.unsuppress('ComplicatedTypeWarning', 'UnpredictableBehaviourWarning')

	assert Configure.suppressed() == {
		"ComplicatedTypeWarning": False,
		"UnpredictableBehaviourWarning": False
	}


	Configure.raise_better_errors(False)
	with pytest.raises(
		LookupError,
		match = "Warning .* not found in warnings list."
	):
		Configure.suppress('ComplicatedTypeWarning', 'TotallyValidWarning')


	with pytest.raises(
		LookupError,
		match = "Warning .* not found in warnings list."
	):
		Configure.unsuppress('ComplicatedTypeWarning', 'TotallyValidWarning')
	

	with pytest.raises(
		TypeError,
		match = r"Configure\.suppress\(\) only takes string arguments\. Current type: .*"
	):
		Configure.suppress('ComplicatedTypeWarning', 1) # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "Literal[1]" cannot be assigned to parameter "args" of type "str" in function "suppress"\
		# 	"Literal[1]" is incompatible with "str"
	

	with pytest.raises(
		TypeError,
		match = r"Configure\.unsuppress\(\) only takes string arguments\. Current type: .*"
	):
		Configure.unsuppress('ComplicatedTypeWarning', 1) # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "Literal[1]" cannot be assigned to parameter "args" of type "str" in function "suppress"\
		# 	"Literal[1]" is incompatible with "str"


# ---------------------------------- Test 2 ---------------------------------- #
def test_raise_better_errors():
	assert isinstance(Configure.raise_better_errors(), bool)


	Configure.raise_better_errors(True)

	assert Configure.raise_better_errors() is True


	Configure.raise_better_errors(False)

	assert Configure.raise_better_errors() is False

	
	with pytest.raises(
		TypeError,
		match = r"Configure\.raise_better_errors\(\) only takes boolean arguments\. Current type: .*"
	):
		Configure.raise_better_errors("True") # pyright: ignore [reportGeneralTypeIssues]
		# Suppressed error:
		# Argument of type "Literal['True']" cannot be assigned to parameter "value" of type "bool | None" in function "raise_better_errors"
		# 	Type "Literal['True']" cannot be assigned to type "bool | None"
		# 		"Literal['True']" is incompatible with "bool"
		# 		Type cannot be assigned to type "None"


# ---------------------------------- Test 3 ---------------------------------- #
def test_illegal_instantiation_error():
	Configure.raise_better_errors(False)

	with pytest.raises(
		IllegalInstantiationError,
		match = r"Configure\(\) class should not be instantiated as an object."
	):
		a_seeminlgy_innocent_object = Configure()