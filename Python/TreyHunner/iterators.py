favorite_numbers = [6, 57, 4, 7, 68, 95]
my_iterator = iter(favorite_numbers)
next(my_iterator)
next(my_iterator)

from itertools import repeat
lots_of_fours = repeat(4, times=100_000_000)
lots_of_fours

import sys
sys.getsizeof(lots_of_fours)

lots_of_fours = [4] * 100_000_000
sys.getsizeof(lots_of_fours)

print(next(open('giant_log_file.txt')))

from itertools import count
for n in count():
    print(n)

class Count:

    """Iterator that counts upward forever."""

    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num



numbers = [1, 2, 3]

str(numbers), numbers.__str__()
len(numbers), numbers.__len__()

c = Count()
next(c)
next(c)
for n in Count():
    if n <= 10:
        print(n)

favorite_numbers = [6, 57, 4, 7, 68, 95]
def square_all(numbers):
     for n in numbers:
         yield n**2

squares = square_all(favorite_numbers)
squares
type(squares)
next(squares)
next(squares)

squares = (n**2 for n in favorite_numbers)
squares
type(squares)
next(squares)
next(squares)


def gimme4_please():
    print("Let me go get that number for you.")
    return 4

num = gimme4_please()
num

def gimme4_later_please():
    print("Let me go get that number for you.")
    yield 4

get4 = gimme4_later_please()
get4

num = next(get4)
num

def count(start=0):
    num = start
    while True:
        yield num
        num += 1

c = count()
next(c)

for n in count():
    if n <= 10:
        print(n)

lines = [ \
    line.rstrip('\n') \
    for line in poem_file \
    if line != '\n' \
]

lines = (
    line.rstrip('\n')
    for line in poem_file
    if line != '\n'
)

def get_a_generator(some_iterable):
    for item in some_iterable:
        if some_condition(item):
            yield item

def get_a_generator(some_iterable):
    return (
        item
        for item in some_iterable
        if some_condition(item)
    )

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __iter__(self):
        yield self.x
        yield self.y

p = Point(1, 2)
x, y = p
print(x, y)
list(p)

