from abc import ABC, abstractmethod
from dataclasses import dataclass
from copy import copy
from typing import List, Dict

@dataclass(slots=True)
class Tensor(ABC):

    """Class to interface a tensor type"""

    @abstractmethod
    def __add__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __sub__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __mul__(self, item):
        raise NotImplementedError

    @abstractmethod
    def __truediv__(self, item):
        raise NotImplementedError

    @abstractmethod
    def reset(self):
        raise NotImplementedError

    @abstractmethod
    def update(self, other):
        raise NotImplementedError


@dataclass(slots=True)
class InertiaTensor(Tensor):

    """ nxn tensor methods """

    def reset(self):
        [self.__setattr__(key, None) for key in self.__slots__]

    def update(self, other) -> None:

        if isinstance(other, list):
            [self.__setattr__(key, other) for (key, other) in zip(self.__slots__, other)]
            return

        elif isinstance(other, dict):
            [self.__setattr__(key, other[key2]) for (key, key2) in zip(self.__slots__, other.keys())]
            return

        elif not self.__class__() == other.__class__():
            raise NotImplementedError(f'Is not of {self.__class__()} type.')
        [self.__setattr__(key, other.__getattribute__(key)) for key in self.__slots__]

    def __add__(self, other):
        if not self.__class__() == other.__class__():
            raise NotImplementedError(f'Is not of {self.__class__()} type.')
        x = copy(self)
        [x.__setattr__(key, self.__getattribute__(key) + other.__getattribute__(key)) for key in self.__slots__]
        return x

    def __sub__(self, other):
        if not self.__class__() == other.__class__():
            raise NotImplementedError(f'Is not of {self.__class__()} type.')
        x = copy(self)
        [x.__setattr__(key, self.__getattribute__(key) - other.__getattribute__(key)) for key in self.__slots__]
        return x

    def __mul__(self, other):
        x = copy(self)
        if isinstance(other, float) or isinstance(other, int):
            [x.__setattr__(key, self.__getattribute__(key) * other) for key in self.__slots__]
        elif isinstance(other, list):
            [x.__setattr__(key, self.__getattribute__(key) * item) for key, item in zip(self.__slots__, other)]
        elif self.__class__() == other.__class__():
            raise NotImplementedError("Can't multiply tensors that way")
        else:
            pass
        return x

    def __truediv__(self, other):
        x = copy(self)
        if isinstance(other, float) or isinstance(other, int):
            [x.__setattr__(key, self.__getattribute__(key) / other) for key in self.__slots__]
        elif isinstance(other, list):
            [x.__setattr__(key, self.__getattribute__(key) / item) for key, item in zip(self.__slots__, other)]
        elif self.__class__() == other.__class__():
            raise NotImplementedError("Can't divide tensors that way")
        else:
            raise NotImplementedError
        return x


@dataclass(slots=True)
class Vector(Tensor):
    """A 1xn tensor"""
    def reset(self):
        [self.__setattr__(key, None) for key in self.__slots__]

    def update(self, other) -> None:
        if isinstance(other, list):
            [self.__setattr__(key, other) for (key, other) in zip(self.__slots__, other)]
            return

        elif isinstance(other, dict):
            [self.__setattr__(key, other[key2]) for (key, key2) in zip(self.__slots__, other.keys())]
            return

        elif not self.__class__() == other.__class__():
            raise NotImplementedError(f'Is not of {self.__class__()} type.')
        [self.__setattr__(key, other.__getattribute__(key)) for key in self.__slots__]

    def __add__(self, other):
        if not self.__class__() == other.__class__():
            raise NotImplementedError(f'Is not of {self.__class__()} type.')
        x = copy(self)
        [x.__setattr__(key, self.__getattribute__(key) + other.__getattribute__(key)) for key in self.__slots__]
        return x

    def __sub__(self, other):
        if not self.__class__() == other.__class__():
            raise NotImplementedError(f'Is not of {self.__class__()} type.')
        x = copy(self)
        [x.__setattr__(key, self.__getattribute__(key) - other.__getattribute__(key)) for key in self.__slots__]
        return x

    def __mul__(self, other):
        if self.__class__() == other.__class__():
            raise NotImplementedError("Can't multiply vectors that way")
        x = copy(self)
        if isinstance(other, float) or isinstance(other, int):
            [x.__setattr__(key, self.__getattribute__(key) * other) for key in self.__slots__]
        elif isinstance(other, list):
            [x.__setattr__(key, self.__getattribute__(key) * item) for key, item in zip(self.__slots__, other)]
        else:
            pass
        return x

    def __truediv__(self, other):
        if self.__class__() == other.__class__():
            raise NotImplementedError("Can't multiply vectors that way")
        x = copy(self)
        if isinstance(other, float) or isinstance(other, int):
            [x.__setattr__(key, self.__getattribute__(key) / other) for key in self.__slots__]
        elif isinstance(other, list):
            [x.__setattr__(key, self.__getattribute__(key) / item) for key, item in zip(self.__slots__, other)]
        else:
            pass
        return x
