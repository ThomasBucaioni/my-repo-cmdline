#!/bin/python3
import random
import numpy as np
import time
import threading
import math as math
import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

pp = pprint.PrettyPrinter(indent=4, width=3)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

m = 'o'
ax.scatter([0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

random.seed(1)
lock = threading.Lock()

def fComputeConfiguration():
    p = random.randint(0, 359)*math.tau/360  # phi
    a = random.randint(-89, 89)*math.tau/360  # alpha
    t = random.randint(0, 359)*math.tau/360  # theta
    p = 45 * math.tau / 360
    a = 35 * math.tau / 360
    t = 90 * math.tau / 360
    v1 = np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])
    ap = a+math.pi/2
    v2 = np.array([math.cos(p)*math.cos(ap), math.sin(p)*math.cos(ap), math.sin(ap)])
    p1 = 100 * v1
    p3 = 100 * v2
    p2 = p1 + p3
    r01 = np.matrix([
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 1]])
    d = math.sqrt(v1[1]**2+v1[2]**2)
    mpB0Bad = np.matrix([
        [0       ,    -d        , v1[0]],
        [ v1[2]/d, v1[0]*v1[2]/d, v1[1]],
        [-v1[1]/d, v1[0]*v1[1]/d, v1[2]]])
    mpBadB0 = mpB0Bad.T
    r02 = np.matmul(mpB0Bad, np.matmul(r01, mpBadB0))
    p22 = np.reshape(np.matmul(r02, p2), 3)
    p32 = np.reshape(np.matmul(r02, p3), 3)
    lock.acquire()
    name=threading.current_thread().name
    print(f'Process name: {name}')
    print(f'Angles: ({p}, {a}, {t})')
    print('-----')
    pp.pprint(f'{v1}')
    print('-----')
    pp.pprint(f'{v2}')
    print('-----')
    pp.pprint(f'{p1}')
    print('-----')
    pp.pprint(f'{p2}')
    print('-----')
    pp.pprint(f'{p3}')
    print('-----')
    print(f'{mpB0Bad}')
    print('-----')
    print(f'{mpBadB0}')
    print('-----')
    print(f'{np.matmul(mpB0Bad, mpBadB0)}')
    print('-----')
    print(f'{r02}')
    print('-----')
    pp.pprint(f'{p22}')
    print('-----')
    pp.pprint(f'{p32}, {np.dot(p32,p32.T)}')
    
    lock.release()

for i in range(1):
    t = threading.Thread(target=fComputeConfiguration, name=f"T{i:0>3d}")
    t.start()


time.sleep(1)
lock.acquire()
print('-----')
print(f"Done launching threads. Thread: {threading.current_thread().name}")
lock.release()
