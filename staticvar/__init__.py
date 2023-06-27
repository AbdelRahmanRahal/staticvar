from .staticvar import staticvar
from .exceptions import (
    StaticvarException,
    IllegalInstantiationError,
    UnsupportedTypeError,
    StaticvarWarning,
    ComplicatedTypeWarning,
    UnpredictableBehaviourWarning
)
from .utils import Configure, StaticvarExceptionHandler


__version__ = "0.1.0"