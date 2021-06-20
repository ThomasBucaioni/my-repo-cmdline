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
import pathlib, os, shutil

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


def fComputeConfigurationDebug():
    p = random.randint(0, 359)*math.tau/360  # phi
    a = random.randint(-89, 89)*math.tau/360  # alpha
    t = random.randint(0, 359)*math.tau/360  # theta
    p = 45 * math.tau / 360
    a = 35 * math.tau / 360
    t = 90 * math.tau / 360
    v1 = -np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])

    lf = 41
    p1 = lf * v1

    u = np.cross(v1, np.array([1, 0, 0]))
    u = u / np.linalg.norm(u)
    v = np.cross(v1, u)

    p3 = lf * u
    p2 = p1 + p3

    d = math.sqrt(v1[1]**2+v1[2]**2)

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


def fCompPhiAlpha(P,l):
    import math
    a = math.asin(P[2]/l)*360/math.tau
    if a > 90:
        a -= 360
    if P[1] != 0:
        p = math.atan(P[1]/P[0])*360/math.tau
        if P[0] < 0:
            p += 180
    else:
        p = 0
    if p < 0:
        p += 360
    print(f'\u03C6={p}, \u03B1={a}')
    return p, a

def fComputeConfiguration():
    pstore = random.randint(0, 359)  # phi
    astore = random.randint(-89, 89)  # alpha
    tstore = random.randint(0, 359)  # theta
    if pstore == 0: pstore = 1
    p = pstore*math.tau/360  # phi
    a = astore*math.tau/360  # alpha
    t = tstore*math.tau/360  # theta
    p = 45 * math.tau / 360
    a = 35 * math.tau / 360
    t = 90 * math.tau / 360
    p = 1 * math.tau / 360
    a = 1 * math.tau / 360
    t = 1 * math.tau / 360
    v1 = np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])

    lf = 41
    p1 = lf * v1

    u = np.cross(v1, np.array([1, 0, 0]))
    if np.linalg.norm(u) != 0:
        u = u / np.linalg.norm(u)
    else:
        u = np.array([0, 1, 0])
    v = np.cross(v1, u)

    p3 = lf * u
    p2 = p1 + p3

    d = math.sqrt(v1[1]**2+v1[2]**2)

    r01 = np.matrix([
        [ math.cos(t), -math.sin(t), 0],
        [ math.sin(t),  math.cos(t), 0],
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
    # Check
    if 0:
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.set_xlim3d(-lf,lf)
        ax.set_ylim3d(-lf,lf)
        ax.set_zlim3d(-lf,lf)
        X = [0, lf, lf,  0, 0,  0,  0,  0, lf, lf, lf, lf, lf,  0, lf, lf,  0]
        Y = [0,  0,  0,  0, 0, lf, lf,  0,  0, lf, lf,  0, lf, lf, lf, lf, lf]
        Z = [0,  0, lf, lf, 0,  0, lf, lf, lf, lf,  0,  0,  0,  0,  0, lf, lf]
        ax.plot(X, Y, Z, color='gray')
        X = [0, lf, lf,  0, 0]
        Y = [0,  0,  0,  0, 0]
        Z = [0,  0, lf, lf, 0]
        ax.plot(X, Y, Z, color='red')
        X = [0, p1[0], p2[0], p3[0], 0]
        Y = [0, p1[1], p2[1], p3[1], 0]
        Z = [0, p1[2], p2[2], p3[2], 0]
        ax.plot(X, Y, Z, color='green')
        X = [0, p1[0], p22[0], p32[0], 0]
        Y = [0, p1[1], p22[1], p32[1], 0]
        Z = [0, p1[2], p22[2], p32[2], 0]
        ax.plot(X, Y, Z, color='orange')
        plt.show()
    
    #-----
    # Lock
    lock.acquire()

    name=threading.current_thread().name
    print(f'Process name: {name}')
    print(f'Angles: ({p}, {a}, {t})')
    print('-----')
    print(f'{v1=}')
    print('-----')
    print(f'{u=}')
    print('-----')
    print(f'{p1=}')
    print('-----')
    print(f'{p2=}')
    print('-----')
    print(f'{p3=}')
    print('-----')
    print(f'mpB0Bad=\n{mpB0Bad}')
    print('-----')
    print(f'mpBadB0=\n{mpBadB0}')
    print('-----')
    print(f'{np.matmul(mpB0Bad, mpBadB0)}')
    print('-----')
    print(f'r02=\n{r02}')
    print('-----')
    print(f'{p22=}')
    print('-----')
    print(f'{p32=}')
    print('-----')
    print(f'{lf=}')
    print('-----')

    phi1,alpha1 = fCompPhiAlpha(p1,lf)
    print(phi1,alpha1)
    print('-----')
    
    phi2,alpha2 = fCompPhiAlpha(p22-p1,lf)
    print(phi2, alpha2)
    print('-----')

    phi3,alpha3 = fCompPhiAlpha(p32-p22,lf)
    print(phi3, alpha3)
    print('-----')
        
    phi4,alpha4 = fCompPhiAlpha(-p32,lf)
    print(phi4, alpha4)
    print('-----')

    pathorg = pathlib.Path.home() / 'tlmscn.dat'
    pathdest = pathlib.Path.home() / 'tlmscn-mod.dat'
    limSimu = 30 * 5.125 + 1 * 4 + 1 * 2.25 + 5
    offsetX = -min(0, p1[0], p22[0], p32[0])
    offsetY = -min(0, p1[1], p22[1], p32[1])
    offsetZ = -min(0, p1[2], p22[2], p32[2])
    print(f'Offset\t: {offsetX=:10.3f}, {offsetY=:10.3f}, {offsetZ=:10.3f}')
    
    deltaX = math.ceil(max(0, p1[0], p22[0], p32[0]) - min(0, p1[0], p22[0], p32[0]))
    deltaY = math.ceil(max(0, p1[1], p22[1], p32[1]) - min(0, p1[1], p22[1], p32[1]))
    deltaZ = math.ceil(max(0, p1[2], p22[2], p32[2]) - min(0, p1[2], p22[2], p32[2]))
    print(f'Delta\t: {deltaX=:4}, {deltaY=:4}, {deltaZ=:4}')

    Nxx = 30+1+1+5+deltaX+5+1+1+30
    Nyy = 30+1+1+5+deltaY+5+1+1+30
    Nzz = 30+1+1+5+deltaZ+5+1+1+30
    print(f'Nnn\t: {Nxx=:7}, {Nyy=:7}, {Nzz=:7}')

    endLimSimuX = 32+5+deltaX+5
    endLimSimuY = 32+5+deltaY+5
    endLimSimuZ = 32+5+deltaZ+5
    print(f'endLimSimu\t: {endLimSimuX=:9}, {endLimSimuY=:9}, {endLimSimuZ=:9}')

    tx = random.randint(5, 995)
    ty = random.randint(5, 995)
    tz = random.randint(5, 995)
    startWireX = 1000*(limSimu + offsetX) + tx
    startWireY = 1000*(limSimu + offsetY) + ty
    startWireZ = 1000*(limSimu + offsetZ) + tz
    print(f'startWire\t: {startWireX=:10.3f}, {startWireY=:10.3f}, {startWireZ=:10.3f}')
    print(f'Transltation\t: {tx=:18}, {ty=:18}, {tz=:18}')

    numLine = 0
    with open(str(pathorg), 'r') as forg:
        with open(str(pathdest), 'w') as fdest:
            for line in forg:
                numLine += 1
                if numLine not in [5, 87, 90, 93, 141, 144, 145, 146, 147]:
                    fdest.write(line)
                else:
                    if numLine == 5:
                        fdest.write(f'\t{Nxx}\t{Nyy}\t{Nzz}\t1000.\n')
                    elif numLine == 87:
                        fdest.write(f'\t1\t30\t31\t32\t{endLimSimuX}\t{endLimSimuX+1}\t{endLimSimuX+1+1}\t{endLimSimuX+1+1+30}\t\n')
                    elif numLine == 90:
                        fdest.write(f'\t1\t30\t31\t32\t{endLimSimuY}\t{endLimSimuY+1}\t{endLimSimuY+1+1}\t{endLimSimuY+1+1+30}\t\n')
                    elif numLine == 93:
                        fdest.write(f'\t1\t30\t31\t32\t{endLimSimuZ}\t{endLimSimuZ+1}\t{endLimSimuZ+1+1}\t{endLimSimuZ+1+1+30}\t\n')
                    elif numLine == 141:
                        fdest.write(f'\t{startWireX:10.3f}\t{startWireY:10.3f}\t{startWireZ:10.3f}\t4\t0\t0\n')
                    elif numLine == 144:
                        fdest.write(f'{phi1:20.10f}\t{alpha1:20.10f}\t10.\t0.\t1000.\t31\n')
                    elif numLine == 145:
                        fdest.write(f'{phi2:20.10f}\t{alpha2:20.10f}\t10.\t0.\t1000.\t31\n')
                    elif numLine == 146:
                        fdest.write(f'{phi3:20.10f}\t{alpha3:20.10f}\t10.\t0.\t1000.\t31\n')
                    elif numLine == 147:
                        fdest.write(f'{phi4:20.10f}\t{alpha4:20.10f}\t10.\t0.\t1000.\t31\n')

    storageDir = str(f'{pstore:03}') + '_' + str(f'{astore:+03}') + '_' + str(f'{tstore:03}') + '_' + str(f'{tx:03}') + '_' + str(f'{ty:03}') + '_' + str(f'{tz:03}')
    pathfinal = pathlib.Path.home() / storageDir
    print(f'{pathfinal=}')
    if not pathfinal.is_dir():
        shutil.os.mkdir(pathfinal)
    shutil.copy(pathdest,pathfinal)
    lock.release()


def fTestPhiAlphaTheta():
    random.seed(time.time())
    while True:
        p = random.randint(0, 359)*math.tau/360  # phi
        a = random.randint(-89, 89)*math.tau/360  # alpha
        t = random.randint(0, 359)*math.tau/360  # theta
        v1 = np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])
        lf = 41
        p1 = lf * v1
        print(f'Angles: p={p*360/math.tau}, a={a*360/math.tau}')
        pc, ac = fCompPhiAlpha(p1,lf)
        a=a/math.tau*360
        p=p/math.tau*360
        if (abs(ac - a) >= 1e-5) or (abs(pc - p) >= 1e-5):
            print(f'BUG: {abs(ac - a)} {abs(pc - p)}\n \
            {a=}, {p=}, \n \
            {ac=}, {pc=}')
            sys.exit(1)
        print(f"-----")  # Norm = {np.linalg.norm(p1)}")


#fTestPhiAlphaTheta()
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
