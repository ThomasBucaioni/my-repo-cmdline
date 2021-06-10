#!/bin/python3
import random
import numpy as np
import time
import threading
import math as math
import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
import matplotlib.animation as animation

pp = pprint.PrettyPrinter(indent=4, width=3)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

m = 'o'
# ax.scatter([0, 100, 0, 0, 100], [0, 0, 100, 0, 100], [0, 0, 0, 100, 100], marker=m)
m = '^'
X = []
Y = []
Z = []
for i in [0,100]:
    for j in [0,100]:
        for k in [0,100]:
            X.append(i)
            Y.append(j)
            Z.append(k)
# ax.plot(X,Y,Z, marker=m)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()


random.seed(1)
lock = threading.Lock()

def update_lines(num, data_lines, lines):
    for line, data in zip(lines, data_lines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

def fComputeConfiguration():
    p = random.randint(0, 359)*math.tau/360  # phi
    a = random.randint(-89, 89)*math.tau/360  # alpha
    t = random.randint(0, 359)*math.tau/360  # theta
    p = 45 * math.tau / 360
    a = 35 * math.tau / 360
    t = 90 * math.tau / 360
    v1 = -np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])
    v1 = np.array([0, 1, 0])
    v1 = np.array([1, 1, 0])/math.sqrt(2)
    v1 = np.array([1, 2, 3])
    v1 = - v1 / np.linalg.norm(v1)
    ap = a+math.pi/2
    v2 = np.array([math.cos(p)*math.cos(ap), math.sin(p)*math.cos(ap), math.sin(ap)])
    v2 = np.array([0, 0, 1])
    #v2 = np.array([1, -1, 0])/math.sqrt(2)
    print(f'Scalar product: <v1,v2> = {np.dot(v1,v2)}')
    p1 = 100 * v1
    p3 = 100 * v2
    p2 = p1 + p3

    u = np.cross(v1, np.array([1, 0, 0]))
    p3 = 100 * u
    p2 = p1 + p3
    u = u / np.linalg.norm(u)
    v = np.cross(v1, u)
    d = math.sqrt(v1[1]**2+v1[2]**2)
    print('-----')
    print(f'{v1=}')
    print(f'{u=}')
    print(f'{v=}')
    print(f'up={[0, v1[2]/d, -v1[1]/d]}')
    print(f'vp={[-d, v1[0]*v1[1]/d, v1[0]*v1[2]/d]}')
    print('-----')
    print(f'Error on u: {np.linalg.norm(u-np.array([0, v1[2]/d, -v1[1]/d]))}')
    print(f'Error on v: {np.linalg.norm(v-np.array([-d, v1[0]*v1[1]/d, v1[0]*v1[2]/d]))}')
    print('-----')
    r01 = np.matrix([
        [ 0,  1, 0],
        [-1,  0, 0],
        [ 0,  0, 1]])
    mpB0Bad = np.matrix([
        [0       ,    -d        , v1[0]],
        [ v1[2]/d, v1[0]*v1[1]/d, v1[1]],
        [-v1[1]/d, v1[0]*v1[2]/d, v1[2]]])
    mpBadB0 = mpB0Bad.T
    r02 = np.matmul(mpB0Bad, np.matmul(r01, mpBadB0))
    p22 = np.squeeze(np.asarray(np.matmul(r02, p2)))
    p32 = np.squeeze(np.asarray(np.matmul(r02, p3)))
    #-----
    # Lock
    #lock.acquire()
    name=threading.current_thread().name
    print(f'Process name: {name}')
    print(f'Angles: ({p}, {a}, {t})')
    print('-----')
    print(f'{v1}')
    print('-----')
    print(f'{v2}')
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
    
    #-----
    # Check
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_xlim3d(-100,100)
    ax.set_ylim3d(-100,100)
    ax.set_zlim3d(-100,100)
    X = [0, 100, 100,   0, 0,   0,   0,   0, 100, 100, 100, 100, 100,   0, 100, 100,   0]
    Y = [0,   0,   0,   0, 0, 100, 100,   0,   0, 100, 100,   0, 100, 100, 100, 100, 100]
    Z = [0,   0, 100, 100, 0,   0, 100, 100, 100, 100,   0,   0,   0,   0,   0, 100, 100]
    ax.plot(X, Y, Z, color='gray')
    X = [0, 100, 100, 0, 0]
    Y = [0, 0, 0, 0, 0]
    Z = [0, 0, 100, 100, 0]
    ax.plot(X, Y, Z, color='red')
    X = [0, p1[0], p2[0], p3[0], 0]
    Y = [0, p1[1], p2[1], p3[1], 0]
    Z = [0, p1[2], p2[2], p3[2], 0]
    ax.plot(X, Y, Z, color='green')
    X = [0, p1[0], p22[0], p32[0], 0]
    Y = [0, p1[1], p22[1], p32[1], 0]
    Z = [0, p1[2], p22[2], p32[2], 0]
    ax.plot(X, Y, Z, color='orange')
    N = 100
    data = []
    print(f'{data=}')
    for i in range(N):
        t = (i+0.25) * math.tau / N
        r01 = np.matrix([
            [math.cos(t), -math.sin(t), 0],
            [math.sin(t),  math.cos(t), 0],
            [          0,            0, 1]])
        r02 = np.matmul(mpB0Bad, np.matmul(r01, mpBadB0))
        p22 = np.squeeze(np.asarray(np.matmul(r02, p2)))
        p32 = np.squeeze(np.asarray(np.matmul(r02, p3)))
        line_data = np.empty((3, 5))
        line_data[:, 0] = np.zeros(3)
        line_data[:, 1] = p1
        line_data[:, 2] = p22
        line_data[:, 3] = p32
        line_data[:, 4] = np.zeros(3)
        data.append(line_data)
        X = [0, p1[0], p22[0], p32[0], 0]
        Y = [0, p1[1], p22[1], p32[1], 0]
        Z = [0, p1[2], p22[2], p32[2], 0]
        #ax.plot(X, Y, Z, color='blue')
    
    lines = [ax.plot(dat[0, 0:5], dat[1, 0:5], dat[2, 0:5])[0] for dat in data]
    line_ani = animation.FuncAnimation(
        fig,
        update_lines,
        6,
        fargs=(data, lines),
        interval=500)
    plt.show()

    #lock.release()

fComputeConfiguration()

for i in range(1):
    #t = threading.Thread(target=fComputeConfiguration, name=f"T{i:0>3d}")
    #t.start()
    pass


time.sleep(1)
lock.acquire()
print('-----')
print(f"Done launching threads. Thread: {threading.current_thread().name}")
lock.release()
