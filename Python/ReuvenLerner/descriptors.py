#!/bin/python3

def hello(a):
    print(a)
    return "Hello!"

class ReturnFunc(object):
    def __get__(self, obj, objtype):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        return hello

class Foo(object):
    x = ReturnFunc()

f = Foo()
s = f.x('a')
print(s)
print("--")
print("End of the fist part")
print("----------")

def hello(self):
    return "Hello from {}!".format(self)

class ReturnFunc(object):
    def __get__(self, obj, objtype):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        return hello(obj)

class Foo(object):
    x = ReturnFunc()

f = Foo()
s = f.x
print(s)
print("--")
print("End of the second part")
print("----------")

from functools import partial

def hello(self):
    return "Hello from {}!".format(self)

class ReturnFunc(object):
    def __get__(self, obj, objtype):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        return partial(hello, obj)

class Foo(object):
    x = ReturnFunc()

f = Foo()
s = f.x()
print(s)
print("--")
print("End of the third part")
print("----------")

from functools import partial

def hello(self):
    return "Hello from {}!".format(self)

class ReturnFunc(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        return partial(self.f, obj)

class Foo(object):
    x = ReturnFunc(hello)

f = Foo()
s = f.x()
print(s)
print("--")
print("End of the fourth part")
print("----------")

from functools import partial

def y2(self):
    return "2 * y = {}".format(self.y * 2)

class ReturnFunc(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        return partial(self.f, obj)

class Foo(object):
    x = ReturnFunc(y2)
    def __init__(self, y):
        self.y = y

f = Foo(20)
s = f.x()
print(s)
print("--")
print("End of the fifth part")
print("----------")

from functools import partial

def muly(self, num):
    return "{} * y = {}".format(num, self.y * num)

class ReturnFunc(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype, *args):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        return partial(self.f, obj, *args)

class Foo(object):
    x = ReturnFunc(muly)
    def __init__(self, y):
        self.y = y

f = Foo(20)
s = f.x(3)

# xFoo.x(f) # error

print(s)
print("--")
print("End of the sixth part")
print("----------")

from functools import partial

def muly(self, num):
    return "{} * y = {}".format(num, self.y * num)

class ReturnFunc(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype, *args):
        print("Invoked __get__")
        print("\tself = {}".format(self))
        print("\tobj = {}".format(obj))
        print("\tobjtype = {}".format(objtype))
        if obj:
            return partial(self.f, obj, *args)
        else:
            return self.f

class Foo(object):
    x = ReturnFunc(muly)
    def __init__(self, y):
        self.y = y


f = Foo(20)
print(f.x(3))
print(Foo.x(f, 3))

print("--")
print("End of the seventh part")
print("----------")

from functools import partial

def muly(self, num):
    return "{} * y = {}".format(num, self.y * num)

class ReturnFunc(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype, *args):
        if obj:
            return partial(self.f, obj, *args)
        else:
            return self.f

class Foo(object):
    x = ReturnFunc(muly)
    def __init__(self, y):
        self.y = y

f = Foo(20)
print(f.x(3))
print(Foo.x(f, 3))
print("--")
print("End")
print("----------")
