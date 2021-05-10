#!/bin/python3

s= 'abc def ghi jkl'
s.count(' ')

filename = 'ideas.txt'

total = 0

for one_line in open(filename):
    total += one_line.count(' ')

def count_spaces(filename):
    total = 0
    for one_line in open(filename):
        total += one_line.count(' ')
    return total

import glob

for one_filename in glob.glob('*.txt'):
    print(count_spaces(one_filename))


def count_spaces_glob(pattern):
    total = 0
    for one_filename in glob.glob(pattern):
        total += count_spaces(one_filename)
    return total

count_spaces_glob('*.txt')

# %timeit count_spaces_glob('*.txt')

import threading
from queue import Queue, Empty

q = Queue()

def count_spaces(filename):
    total = 0
    for one_line in open(filename):
        total += one_line.count(' ')
    q.put(total)

def count_spaces_glob(pattern):
    for one_filename in glob.glob(pattern):
        t = threading.Thread(target=count_spaces, args=(one_filename,))
        t.start()

    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():

            if threading.current_thread() == t:
                continue

            t.join(0.1)
    print("All threads are done")

    total = 0
    while True:
        try:
            total += q.get(True, 0.01)
        except Empty as e:
            break

    return total

print(count_spaces_glob('*.txt'))


def total_counts():
    total = 0
    while True:
        try:
            total += q.get(True, 0.01)
        except Empty as e:
            break
    print(total)

def count_spaces_glob(pattern):
    for one_filename in glob.glob(pattern):
        t = threading.Thread(target=count_spaces, args=(one_filename,))
        t.start()

    threading.Thread(target=total_counts).start()

    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():

            if threading.current_thread() == t:
                continue

            t.join(0.1)
