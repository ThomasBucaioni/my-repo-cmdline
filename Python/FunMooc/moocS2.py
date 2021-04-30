print(1**2)
print(2**2)
print(3**2)
for i in range(10):
    print(i**2)
for i in ['a', 3.5, True]:
    print(i)
a = [1, 2, 5, 8, 9]
for i in a:
    print(i**2)
b = [3.6, 18, 12, 25]
for i in b:
    print(i**2)
def carre(a):
    for i in a:
        print(i**2)
carre(a)
carre(b)
def carre(a):
    L = []
    for i in a:
        L.append(i**2)
    return L
carre(b)
b = carre(b)
b

a = [1, 4, 18, 29, 13]
import math
b = []
for i in a:
    b.append(math.log(i))
b
b = [math.log(i) for i in a]
b
a.append(-1)
a
b = [math.log(i) for i in a if i > 0]
b
prenom = ['Alice', 'evE', 'sonia', 'BOB']
prenom
prenom = [p.lower() for p in prenom]
prenom

import random
print(random)
dir(random)
help(random)
random.randint? # error
help(random.randint)
random.randint(1, 100)
