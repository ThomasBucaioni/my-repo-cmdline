numbers = range(3, 22)

print(numbers)

squared_odds = [
    n**2
    for n in numbers
    if n % 2 == 1
]

print(squared_odds)

# Looping in Python

# var colors = ["red", "green", "blue", "purple"];
# for (var i = 0; i < colors.length; i++) {
#     console.log(colors[i]);
# }

i = 0
while i < len(colors):
    print(colors[i])
    i += 1

for i in range(len(colors)):
    print(colors[i])

for color in colors:
    print(color)

# range of length
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for i in range(len(presidents)):
    print("President {}: {}".format(i + 1, presidents[i]))

# enumerate
presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents, start=1):
    print("President {}: {}".format(num, name))

colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))

# zip
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]
for color, ratio in zip(colors, ratios):
    print("{}% {}".format(ratio * 100, color))


# Iterables
from itertools import count
multiples_of_five = count(step=5)

for n in multiples_of_five:
    if n > 100:
        break
    print(n)

# Iterators
iterator = iter('hi')
next(iterator)
# 'h'
next(iterator)
# 'i'
next(iterator)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#StopIteration

iterator2 = iter(iterator)
iterator is iterator2
#True


# Looping with iterators
def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break  # Iterator exhausted: stop the loop
        else:
            print(item)
            
print_each({1, 2, 3})

def print_each(iterable):
    for item in iterable:
        print(item)
