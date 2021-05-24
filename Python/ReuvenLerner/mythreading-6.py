#!/usr/bin/env python3

import threading
import time
import random

def bad_division(y):
    print("Thread {}".format(threading.get_ident()))
    time.sleep(random.randint(1, 5))

    x = 10

    z = x / y
    print("\t{}".format(z))

# for i in range(5):
#     t = threading.Thread(target=bad_division, args=(i,))
#     t.start()

# for i in range(5):
#         try:    # doesn't actually work
#             t = threading.Thread(target=bad_division, args=(i,))
#             t.start()
#         except Exception as e:
#             print("Exception {} in thread {}".format(e, t))


def bad_division(y):
    print("Thread {}".format(threading.get_ident()))
    time.sleep(random.randint(1, 5))

    try:
        x = 10
        z = x / y
        print("\t{}".format(z))
    except ZeroDivisionError as e:
        print("Exception {} in thread {}".format(e, threading.get_ident()))


for i in range(5):
    t = threading.Thread(target=bad_division, args=(i,))
    t.start()

threads = []
for i in range(5):
    t = threading.Thread(target=bad_division, args=(i,))
    t.start()
    threads.append(t)

for one_thread in threads:
    one_thread.join()

print("All done!")


from queue import Queue
failure_queue = Queue()

def bad_division(y):
    print("Thread {}".format(threading.get_ident()))
    time.sleep(random.randint(1, 5))

    try:
        x = 10
        z = x / y
        print("\t{}".format(z))
    except ZeroDivisionError as e:
        failure_queue.put((e, threading.get_ident(), x, y))

threads = []

for i in range(5):
    t = threading.Thread(target=bad_division, args=(i,))
    t.start()
    threads.append(t)

for one_thread in threads:
    one_thread.join()

print("All done!")

print("Now showing {} failure(s):".format(failure_queue.qsize()))
while not failure_queue.empty():
    e, tid, x, y = failure_queue.get()
    print("\tThread {}, exception {}: {} / {}".format(tid, e, x, y))
