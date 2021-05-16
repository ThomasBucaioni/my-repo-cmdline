import random
import test_lsp_mode_module as tlmm

for i in range(10):
    print(random.randrange(10), end='\n')


a = 0
b = 2
c_test_refactor_rename = a+b

s = random.random()

t = random.gauss(0,1)

u = random.expovariate(1)

import sys

print(sys.float_info)
sys.float_info

a = c_test_refactor_rename

class my_other_class():
    temperature = 0
    print('A')
    def __init__(self, t):
        self.temperature = t

    print('B')

    def print_t(self):
        print(self.temperature)

    print('C')

    def fib2(self, n):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a+b
        return result

p = my_other_class(5)
print(p)
print(p.fib2(9))
p.print_t()

p = tlmm.my_class(2)
print(p.temperature)
p.printt()

