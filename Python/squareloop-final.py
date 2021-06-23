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
import subprocess
from subprocess import PIPE
import re

pp = pprint.PrettyPrinter(indent=4, width=3)

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# m = 'o'
# # ax.scatter([0, 100, 0, 0, 100], [0, 0, 100, 0, 100], [0, 0, 0, 100, 100], marker=m)
# m = '^'
# X = []
# Y = []
# Z = []
# for i in [0,100]:
#     for j in [0,100]:
#         for k in [0,100]:
#             X.append(i)
#             Y.append(j)
#             Z.append(k)
#             # ax.plot(X,Y,Z, marker=m)

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()


random.seed(1)
lock = threading.Lock()

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
    # print(f'\u03C6={p}, \u03B1={a}')
    return p, a

def fComputeConfiguration():
    pstore = random.randint(0, 359)  # phi
    astore = random.randint(-89, 89)  # alpha
    tstore = random.randint(0, 359)  # theta
    if pstore == 0: pstore = 1
    p = pstore*math.tau/360  # phi
    a = astore*math.tau/360  # alpha
    t = tstore*math.tau/360  # theta
    # p = 45 * math.tau / 360
    # a = 35 * math.tau / 360
    # t = 90 * math.tau / 360
    # p = 1 * math.tau / 360
    # a = 1 * math.tau / 360
    # t = 1 * math.tau / 360
    v1 = np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])

    lf = 31
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
    #-----
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
    #-----
    lock.acquire()

    name=threading.current_thread().name
    # print(f'Process name: {name}')
    # print(f'Angles: ({p}, {a}, {t})')
    # print('-----')
    # print(f'{v1}')
    # print('-----')
    # print(f'{u}')
    # print('-----')
    # print(f'{p1}')
    # print('-----')
    # print(f'{p2}')
    # print('-----')
    # print(f'{p3}')
    # print('-----')
    # print(f'mpB0Bad=\n{mpB0Bad}')
    # print('-----')
    # print(f'mpBadB0=\n{mpBadB0}')
    # print('-----')
    # print(f'{np.matmul(mpB0Bad, mpBadB0)}')
    # print('-----')
    # print(f'r02=\n{r02}')
    # print('-----')
    # print(f'{p22}')
    # print('-----')
    # print(f'{p32}')
    # print('-----')
    # print(f'{lf}')
    # print('-----')

    phi1,alpha1 = fCompPhiAlpha(p1,lf)
    # print(phi1,alpha1)
    # print('-----')
    
    phi2,alpha2 = fCompPhiAlpha(p22-p1,lf)
    # print(phi2, alpha2)
    # print('-----')

    phi3,alpha3 = fCompPhiAlpha(p32-p22,lf)
    # print(phi3, alpha3)
    # print('-----')
        
    phi4,alpha4 = fCompPhiAlpha(-p32,lf)
    # print(phi4, alpha4)
    # print('-----')

    # print('---------')
    # print('-----')
    # print('Initialisation of file tlmscn.dat')
    # print('-----')
    limSimu = 30 * 5.125 + 1 * 4 + 1 * 2.25 + 5
    offsetX = -min(0, p1[0], p22[0], p32[0])
    offsetY = -min(0, p1[1], p22[1], p32[1])
    offsetZ = -min(0, p1[2], p22[2], p32[2])
    # print(f'Offset\t: {offsetX:10.3f}, {offsetY:10.3f}, {offsetZ:10.3f}')
    
    deltaX = math.ceil(max(0, p1[0], p22[0], p32[0]) - min(0, p1[0], p22[0], p32[0]))
    deltaY = math.ceil(max(0, p1[1], p22[1], p32[1]) - min(0, p1[1], p22[1], p32[1]))
    deltaZ = math.ceil(max(0, p1[2], p22[2], p32[2]) - min(0, p1[2], p22[2], p32[2]))
    # print(f'Delta\t: {deltaX:4}, {deltaY:4}, {deltaZ:4}')

    Nxx = 30+1+1+5+deltaX+5+1+1+30
    Nyy = 30+1+1+5+deltaY+5+1+1+30
    Nzz = 30+1+1+5+deltaZ+5+1+1+30
    # print(f'Nnn\t: {Nxx:7}, {Nyy:7}, {Nzz:7}')

    endLimSimuX = 32+5+deltaX+5
    endLimSimuY = 32+5+deltaY+5
    endLimSimuZ = 32+5+deltaZ+5
    # print(f'endLimSimu\t: {endLimSimuX:9}, {endLimSimuY:9}, {endLimSimuZ:9}')

    tx = random.randint(20, 980)
    ty = random.randint(20, 980)
    tz = random.randint(20, 980)
    startWireX = 1000*(limSimu + offsetX) + tx
    startWireY = 1000*(limSimu + offsetY) + ty
    startWireZ = 1000*(limSimu + offsetZ) + tz
    # print(f'startWire\t: {startWireX:10.3f}, {startWireY:10.3f}, {startWireZ:10.3f}')
    # print(f'Transltation\t: {tx:18}, {ty:18}, {tz:18}')

    storageDir = str(f'{pstore:03}') + '_' + str(f'{astore:+03}') + '_' + str(f'{tstore:03}') + '_' + str(f'{tx:03}') + '_' + str(f'{ty:03}') + '_' + str(f'{tz:03}')
    pathcomputation = originaworkingpath / storageDir
    pathdesttlmscn = pathcomputation / 'tlmscn.dat'
    pathdotout =  pathcomputation / 'squareloop_31m.out'
    pathtestoutput = pathcomputation / 'ExecutionTermineeNormalement.txt'
    # print(f'{storageDir}')
    # print(f'{pathdesttlmscn}')
    if not pathcomputation.is_dir():
        shutil.os.mkdir(pathcomputation)
    shutil.copy(originaltlmscnexec, pathcomputation)
    shutil.copy(originaltlmscnjob, pathcomputation)

    numLine = 0
    with open(str(originaltlmscndat), 'r') as forg:
        with open(str(pathdesttlmscn), 'w') as fdest:
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

    os.chdir(pathcomputation)
    # print('-----')
    # print('----------')
    # print('-----')
    # print(f'Start of the job for thread {name}')
    # print('-----')
    bBatchLaunched = False
    while not bBatchLaunched:

        result = subprocess.run(["sbatch", "job.slurm"], stdout=PIPE, stderr=PIPE, universal_newlines=True) #, capture_output=True, text=True)
        print('sbatch stdout:', result.stdout)
        print('sbatch stderr:', result.stderr)
        print('sbatch returncode: ', result.returncode)

        numJob = result.stdout.split(' ')[-1].strip()
        print(f'Number of the job: >{numJob}<\n')

        # result = subprocess.run(["scancel", f'{numJob}'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        # result = subprocess.run(["squeue", f'-j {numJob}'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        # print('scancel stdout:', result.stdout)
        # print('scancel stderr:', result.stderr)
        # print('scancel returncode: ', result.returncode)
        # exit(1)

        if result.returncode != 0:
            print('Job not launched, sleeping 10 sec')
            lock.release()
            time.sleep(10)
            lock.acquire()
        else:
            result = subprocess.run(["sacct", "-u tbucaioni"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
            print('stdout:', result.stdout)
            bBatchLaunched = True
            # re.search()

    print(f"Tread: {name}, job {numJob} running. Releasing the lock")
    print('-----')
    lock.release()
    # bWait = True
    while True:
        result = subprocess.run(["squeue", f"-j {numJob}"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        # print('sacct stdout:', result.stdout)
        # print('sacct stderr:', result.stderr)
        stdoutLines = result.stdout.split('\n')
        if len(stdoutLines) > 2:
            lock.acquire()
            print(f'Tread: {name} |---| Job: {stdoutLines[1].strip()} |---| {storageDir}')
            lock.release()
            if pathdotout.exists():
                with open(pathdotout, 'r') as fCheck:
                    # print('Check erreur squareloop_31m.out')
                    for line in fCheck:
                        match = re.search('Problème|Erreur', line)
                        if match:
                            print(f"Cancel simulation: error detected. Job number >{numJob}< to scancel")
                            result = subprocess.run([f"scancel", f"{numJob}"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
                            lock.acquire()
                            print('scancel stdout:', result.stdout)
                            print('scancel stderr:', result.stderr)
                            lock.release()
            # print(f'Tread {name} sleeping for 10 seconds')
            time.sleep(10)  # in seconds
        else: break
    if not pathtestoutput.exists():
        lock.acquire()
        print(f'Problem with process {numJob} for configuration {storageDir}')
        with open(pathproblemsconfig,'a') as fPb:
            fPb.write(f'{storageDir}\n')
            shutil.copy(pathdesttlmscn, pathproblemsdir / storageDir)
        lock.release()
    else:
        shutil.copy(pathcomputation / 'GENEFILMINCE0001', pathgenedir / f'gene_{storageDir}_squareloop')
        shutil.copy(pathcomputation / 'S11_TFR_GENEFILMINCE0001', paths11dir / f's11_{storageDir}_squareloop')
        for fileToDelete in pathcomputation.glob("*"):
            if str(fileToDelete).split('/')[-1] not in ["GENEFILMINCE0001", "S11_TFR_GENEFILMINCE0001", "tlmscn.dat", "squareloop_31m.out"]:
                os.unlink(fileToDelete)
                # print(f"File to delete: {fileToDelete}")
            else:
                print(f"---> File to keep: {fileToDelete} <---")
                
    # result = subprocess.run(["scancel", f'-n {numJob}'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # print('stdout:', result.stdout)
    # print('returncode: ', result.returncode)
    # result = subprocess.run(["sacct", "-u tbucaioni"], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    # print('stdout:', result.stdout)


def fTestPhiAlphaTheta():
    random.seed(time.time())
    while True:
        p = random.randint(0, 359)*math.tau/360  # phi
        a = random.randint(-89, 89)*math.tau/360  # alpha
        t = random.randint(0, 359)*math.tau/360  # theta
        v1 = np.array([math.cos(p)*math.cos(a), math.sin(p)*math.cos(a), math.sin(a)])
        lf = 31
        p1 = lf * v1
        print(f'Angles: p={p*360/math.tau}, a={a*360/math.tau}')
        pc, ac = fCompPhiAlpha(p1,lf)
        a=a/math.tau*360
        p=p/math.tau*360
        if (abs(ac - a) >= 1e-5) or (abs(pc - p) >= 1e-5):
            print(f'BUG: {abs(ac - a)} {abs(pc - p)}\n \
            {a}, {p}, \n \
            {ac}, {pc}')
            sys.exit(1)
        print(f"-----")  # Norm = np.linalg.norm(p1)


#fTestPhiAlphaTheta()  # Test the reconstruction of phi, alpha, and theta

originaworkingdir = os.getcwd()  # type string
originaworkingpath = pathlib.Path(originaworkingdir)  # type path
originaltlmscndat = originaworkingpath / 'tlmscn.dat'
pathproblemsconfig = originaworkingpath / 'problems.txt'
pathproblemsdir = originaworkingpath / 'ProblemConfigs'
paths11dir = originaworkingpath / 'S11Dir'
pathgenedir = originaworkingpath / 'GeneDir'

# somefiles = originaworkingpath.glob("*")
# print(somefiles)
# listfiles = list[somefiles]
# print(listfiles)
# for fileToDelete in somefiles:
#     if str(fileToDelete).split('/')[-1] not in ["GENEFILMINCE0001", "S11_TFR_GENEFILMINCE0001", "tlmscn.dat"]:
#         print(f"File to delete: {fileToDelete}")
# exit(1)

if not pathproblemsdir.exists():
    shutil.os.mkdir(pathproblemsdir)
if not pathgenedir.exists():
    shutil.os.mkdir(pathgenedir)
if not paths11dir.exists():
    shutil.os.mkdir(paths11dir)
    
if not originaltlmscndat.exists():
    print('No data file. Exiting')
    exit(1)
originaltlmscnexec = originaworkingpath / 'tlmscn2'
if not originaltlmscnexec.exists():
    print('No exec file. Exiting')
    exit(1)
originaltlmscnjob = originaworkingpath / 'job.slurm'
if not originaltlmscnjob.exists():
    print('No job file. Exiting')
    exit(1)
    
# a = os.getcwd()
# print(type(a), a)
# a = a + "/subdir"
# mypath = pathlib.Path(a)
# print(a, mypath)
# if not mypath.is_dir():
#     shutil.os.mkdir(mypath)
# os.chdir(mypath)
# import datetime as dt
# a = 'testfile' + str(dt.datetime.now()).replace(" ", "_")
# with open(a,'a') as f:
#     f.write(a)
#fComputeConfiguration()

random.seed(time.time())
#random.seed(1)
i = 0
while i < 400:
    i = len(list(pathgenedir.glob("*")))
    print('Nb curves: ', i)
    t = threading.Thread(target=fComputeConfiguration, name=f"T{i:0>3d}")
    t.start()
    t.join()
#    time.sleep(3*60)


time.sleep(1)
lock.acquire()
print('-----')
print(f"Done launching threads. Thread: {threading.current_thread().name}")
print('-----')
lock.release()
