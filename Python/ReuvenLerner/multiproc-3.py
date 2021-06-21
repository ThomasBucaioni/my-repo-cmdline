#!/bin/python3

import multiprocessing
import time
import random

def write_abc(filename, i):
    print("Writing to {} with i = {}".format(filename, i))
    with open(filename, 'a') as f:
        for word in 'abc def ghi jkl mno'.split():
            time.sleep(random.randint(1,3))
            f.write("{}: {}\n".format(i, word))
            f.flush()

# for i in range(5):
#     multiprocessing.Process(target=write_abc, args=('/tmp/stuff.txt', i)).start()


from multiprocessing import Lock

lock = Lock()

def write_abc(filename, i):
    print("Writing to {} with i = {}".format(filename, i))
    lock.acquire()
    with open(filename, 'a') as f:
        for word in 'abc def ghi jkl mno'.split():
            time.sleep(random.randint(1,3))
            f.write("{}: {}\n".format(i, word))
            f.flush()
    lock.release()

for i in range(5):
    multiprocessing.Process(target=write_abc, args=('/tmp/stuff.txt', i)).start()

