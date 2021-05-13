#!/bin/python3

class NbAppels:
    def __init__(self, f):
        self.appels = 0
        self.f = f
    def __call__(self, *t, **d):
        self.appels += 1
        s = f"Function {self.f.__name__} has been called {self.appels} time(s)"
        print(s)
        return self.f(*t, **d)

@NbAppels
def f(a, b):
    print(f'Arguments of f: {a}, {b}')


f(1, 2)

f(3, 'a')

@NbAppels
def g(a, b, c):
    print(f'Arguments of f: {a}, {b}, {c}')
    
g(1, 2, 3)

#

