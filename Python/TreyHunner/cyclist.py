#!/bin/python3
class CyclicSequenceIterator:

    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.sequence[self.index]
        self.index += 1
        self.index %= len(self.sequence)
        return value

class CyclicList:

    """List-like data structure that loops in a cyclic manner."""

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return CyclicSequenceIterator(self.data)

class CyclicList:

    """List-like data structure that loops in a cyclic manner."""

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        i = 0
        while True:
            yield self.data[i]
            i = (i + 1) % len(self.data)

from itertools import cycle


class CyclicList:

    """List-like data structure that loops in a cyclic manner."""

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return cycle(self.data)

#
from itertools import cycle


class CyclicList:

    """List-like data structure that loops in a cyclic manner."""

    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return cycle(self.data)

    def __len__(self):
        return len(self.data)

    def append(self, item):
        self.data.append(item)

    def pop(self, *args, **kwargs):
        return self.data.pop(*args, **kwargs)

class CyclicList(list):

    """List-like data structure that loops in a cyclic manner."""

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i = (i + 1) % len(self)

from collections import UserList
from itertools import cycle


class CyclicList(UserList):

    """List-like data structure that loops in a cyclic manner."""

    def __iter__(self):
        return cycle(self.data)

#
from collections import UserList
from itertools import cycle


class CyclicList(UserList):

    """List-like data structure that loops in a cyclic manner."""

    def __iter__(self):
        return cycle(self.data)

    def __getitem__(self, index):
        return self.data[index % len(self)]

    def __setitem__(self, index, value):
        self.data[index % len(self)] = value

from itertools import count


class CyclicList(list):

    """List-like data structure that loops in a cyclic manner."""

    def __iter__(self):
        for i in count():
            yield self[i]

    def __getitem__(self, index):
        return super().__getitem__(index % len(self))

    def __setitem__(self, index, value):
        return super().__setitem__(index % len(self), value)

from collections import UserList
from itertools import cycle


class CyclicList(UserList):

    """List-like data structure that loops in a cyclic manner."""

    def __iter__(self):
        return cycle(self.data)

    def __getitem__(self, index):
        return super().__getitem__(index % len(self))

    def __setitem__(self, i, v):
        return super().__setitem__(i % len(self), v)

from collections import UserList
from itertools import cycle


class CyclicList(UserList):

    """List-like data structure that loops in a cyclic manner."""

    def __getitem__(self, index):
        return super().__getitem__(index % len(self))

    def __setitem__(self, i, v):
        return super().__setitem__(i % len(self), v)

class CyclicList:

    """List-like data structure that loops in a cyclic manner."""

    def __init__(self, data):
        self.data = list(data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index % len(self)]

    def __setitem__(self, index, value):
        self.data[index % len(self)] = value

    def append(self, item):
        self.data.append(item)

    def pop(self, index=-1):
        return self.data.pop(index)

#
def __getitem__(self, index):
        if isinstance(index, slice):
            start = index.start
            stop = index.stop
            if start is None:
                start = 0
            if stop is None:
                if start >= 0:
                    stop = len(self)
                else:
                    stop = 0
            return [self[i] for i in range(start, stop)]
        return self.data[index % len(self)]
    
    def _slice_indices(self, obj):
        start, stop = obj.start, obj.stop
        if obj.step is not None:
            raise ValueError("Step not supported")
        if start is None:
            start = 0
        if stop is None:
            stop = len(self) if start >= 0 else 0
        return start, stop, 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [
                self[i]
                for i in range(*self._slice_indices(index))
            ]
        return self.data[index % len(self)]

class CyclicList(list):
    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i = (i + 1) % len(self)

    def _slice_indices(self, obj):
        start, stop = obj.start, obj.stop
        if obj.step is not None:
            raise ValueError("Step not supported")
        if start is None:
            start = 0
        if stop is None:
            stop = len(self) if start >= 0 else 0
        return start, stop, 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [
                self[i]
                for i in range(*self._slice_indices(index))
            ]
        return super().__getitem__(index % len(self))

    def __setitem__(self, index, value):
        super().__setitem__(index % len(self), value)

from collections import UserList


class CyclicList(UserList):
    def _slice_indices(self, obj):
        start, stop = obj.start, obj.stop
        if obj.step is not None:
            raise ValueError("Step not supported")
        if start is None:
            start = 0
        if stop is None:
            stop = len(self) if start >= 0 else 0
        return start, stop, 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [
                self[i]
                for i in range(*self._slice_indices(index))
            ]
        return self.data[index % len(self)]

    def __setitem__(self, index, value):
        self.data[index % len(self)] = value


from collections.abc import MutableSequence


class CyclicList(MutableSequence):

    def __init__(self, data):
        self.data = list(data)

    def _slice_indices(self, obj):
        start, stop = obj.start, obj.stop
        if obj.step is not None:
            raise ValueError("Step not supported")
        if start is None:
            start = 0
        if stop is None:
            stop = len(self) if start >= 0 else 0
        return start, stop, 1

    def __getitem__(self, index):
        if isinstance(index, slice):
            return [
                self[i]
                for i in range(*self._slice_indices(index))
            ]
        return self.data[index % len(self)]

    def __setitem__(self, index, value):
        self.data[index % len(self)] = value

    def __delitem__(self, index):
        del self.data[index % len(self)]

    def __len__(self):
        return len(self.data)

    def insert(self, index, value):
        self.data.insert(index, value)

