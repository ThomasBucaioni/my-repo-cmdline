#!/bin/python3

import threading

x = 12345
y = 'hello'
z = [10, 20, 30]

class MyClass(threading.Thread):

    def run(self):
        tid = threading.get_ident()
        print("Thread {0} has x = {1}, y = {2}, z = {3}".format(tid, x,y,z))

for i in range(5):
    t = MyClass()
    t.start()

print('----------')

import time
import random
import threading

class BadQueue(object):
    def __init__(self):
        self.queue = [ ]
    def append(self, x):
        self.queue.append(x)
    def extend(self, x):
        print("Adding {}\n".format(list(x)))
        for one_item in x:
            time.sleep(random.randint(1,3))
            self.queue.append(one_item)
    def __len__(self):
        return len(self.queue)
    def __repr__(self):
        return "BadQueue: {}".format(self.queue)

def add_to_queue(q, items):
    q.extend(items)

bq = BadQueue()
threads = []

for i in range(3):
    t = threading.Thread(target=add_to_queue, args=(bq, range(10)))
    threads.append(t)
    t.start()

for one_thread in threads:
    one_thread.join()

print(bq)
print('----------')

# with lock

lock = threading.Lock()

class BadQueue(object):
    def __init__(self):
        self.queue = [ ]
    def append(self, x):
        self.queue.append(x)
    def extend(self, x):
        print("Adding {}\n".format(x))
        lock.acquire()
        for one_item in x:
            time.sleep(random.randint(1,2))
            self.queue.append(one_item)
        lock.release()
    def __len__(self):
        return len(self.queue)
    def __repr__(self):
        return "BadQueue: {}".format(self.queue)

def add_to_queue(q, items):
    q.extend(items)

bq = BadQueue()
threads = []

for i in range(2):
    t = threading.Thread(target=add_to_queue, args=(bq, range(10)))
    threads.append(t)
    t.start()

for one_thread in threads:
    one_thread.join()

print(bq)
print('----------')

# with 'with' statement

class BadQueue(object):
    def __init__(self):
        self.queue = [ ]
    def append(self, x):
        self.queue.append(x)
    def extend(self, x):
        print("Adding {}\n".format(x))
        with lock:
            for one_item in x:
                time.sleep(random.randint(1,2))
                self.queue.append(one_item)

    def __len__(self):
        return len(self.queue)
    def __repr__(self):
        return "BadQueue: {}".format(self.queue)

def add_to_queue(q, items):
    q.extend(items)

bq = BadQueue()
threads = []

for i in range(3):
    t = threading.Thread(target=add_to_queue, args=(bq, range(10)))
    threads.append(t)
    t.start()

for one_thread in threads:
    one_thread.join()

print(bq)
print('----------')

