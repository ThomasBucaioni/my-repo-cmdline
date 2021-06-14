#!/usr/bin/env python3

def mysum(numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total

if __name__ == '__main__':
    for i in range(10):
        print(i, mysum(range(i)))

import multiprocessing

def mysum(numbers):
    total = 0
    for one_number in numbers:
        total += one_number
    return total

if __name__ == '__main__':
    for i in range(10):
        print(i, multiprocessing.Process(target=mysum, args=(range(i),)).start())

from multiprocessing import Queue

def mysum(q, i, numbers):
    total = 0
    for one_number in numbers:
        total += one_number
        q.put((i, total))

if __name__ == '__main__':
    processes = []
    q = Queue()

    for i in range(10):
        p = multiprocessing.Process(target=mysum, args=(q, i, range(i)))
        processes.append(p)
        p.start()

    for one_process in processes:
        one_process.join()

    n = 0
    while True:
        print(q.get())
        n = n+1
        print(n)
        if n == 45: break


if __name__ == '__main__':
    processes = []
    q = Queue()

    for i in range(10):
        p = multiprocessing.Process(target=mysum, args=(q, i, range(i)))
        processes.append(p)
        p.start()

    for one_process in processes:
        one_process.join()

    while not q.empty():
        print(q.get())
