#!/bin/python3
def record_calls(func):
    """Record calls to the given function."""
    def wrapper(*args):
        wrapper.call_count += 1
        return func(*args)
    wrapper.call_count = 0
    return wrapper

def record_calls(func):
    """Record calls to the given function."""
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

class record_calls:

    """Record calls to the given function."""

    def __init__(self, func):
        self.call_count = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)

#1
    
def record_calls(func):
"""Record calls to the given function."""
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.__name__ = func.__name__
    wrapper.__qualname__ = func.__qualname__
    wrapper.__doc__ = func.__doc__
    wrapper.__annotations__ = func.__annotations__
    return wrapper

def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

from functools import update_wrapper


class record_calls:

    """Record calls to the given function."""

    def __init__(self, func):
        self.call_count = 0
        self.func = func
        update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)

import wrapt


class record_calls(wrapt.ObjectProxy):

    """Record calls to the given function."""

    def __init__(self, func):
        super().__init__(func)
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.__wrapped__(*args, **kwargs)

#2

from functools import wraps


class Call:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

from collections import namedtuple
from functools import wraps


Call = namedtuple('Call', 'args kwargs')


def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

from typing import NamedTuple
from functools import wraps


class Call(NamedTuple):
    args: tuple
    kwargs: dict


def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

from dataclasses import dataclass
from functools import wraps


@dataclass
class Call:
    args: tuple
    kwargs: dict


def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        wrapper.calls.append(Call(args, kwargs))
        return func(*args, **kwargs)
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


#3

NO_RETURN = object()

def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        call = Call(args, kwargs)
        wrapper.calls.append(call)
        try:
            call.exception = None
            call.return_value = func(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            call.return_value = NO_RETURN
            raise
        return call.return_value
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper

from dataclasses import dataclass
from functools import wraps
from typing import Any, Optional


NO_RETURN = object()


@dataclass
class Call:
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None


def record_calls(func):
    """Record calls to the given function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        call = Call(args, kwargs)
        wrapper.calls.append(call)
        try:
            call.return_value = func(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            raise
        return call.return_value
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper
