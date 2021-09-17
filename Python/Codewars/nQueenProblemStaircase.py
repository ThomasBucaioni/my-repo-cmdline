N = 9
x = [0] * N

# Testing size=9, fixed=(3, 8)
# Testing size=9, fixed=(7, 3)
# Testing size=10, fixed=(2, 0)
# Testing size=11, fixed=(2, 8)
# Testing size=18, fixed=(16, 3)
# Testing size=24, fixed=(22, 10)
# Testing size=27, fixed=(11, 8)
# Testing size=50, fixed=(36, 35)
# Testing size=136, fixed=(111, 76)
# Testing size=228, fixed=(193, 34)
# Testing size=323, fixed=(320, 133)
# Testing size=444, fixed=(121, 99)
# Testing size=499, fixed=(68, 120)
# Testing size=524, fixed=(259, 280)
# Testing size=669, fixed=(538, 655)
# Testing size=799, fixed=(238, 429)
# Testing size=875, fixed=(235, 79)
# Testing size=975, fixed=(766, 381)

import numpy as np

def print_board(i):
    #print(N)
    b = np.zeros((N,N),dtype=str)
    #print(b)
    for k in range(N):
        for j in range(N):
            b[k,j] = '-'
    #print(b)
    # for k in range(8):
    #     print(b[k])
    for k in range(N):
        if k <= i:
            for l in range(N):
                b[k,l] = 'x'
                b[l,x[k]] = 'x'
                if k-l >= 0:
                    if x[k]-l >= 0:
                        b[k-l,x[k]-l] = 'x'
                    if x[k]+l <= N-1:
                        b[k-l,x[k]+l] = 'x'
                if k+l <= N-1:
                    if x[k]+l <= N-1:
                        b[k+l,x[k]+l] = 'x'
                    if x[k]-l >= 0:
                        b[k+l,x[k]-l] = 'x'
    for k in range(N):
        if k <= i:
            b[k,x[k]] = 'Q'
    print(b)

l = []
for i in range(1,N+1):
    if (i % 2) == 1:
        l.append(i)
    else:
        l.insert(int(i/2)-1,i)
print(f'{l=}')

r = N % 6
if r == 2:
    n = int(N/2)
    a = l[n]
    l[n] = l[n+1]
    l[n+1] = a
    l.remove(5)
    l.append(5)
print(f'{l=}')

for i in range(N):
    x[l[i]-1] = i

print(f'{x=}')
print_board(N)


def rot(N,t):
    # print(N, t)
    centre = np.array([[N/2], [N/2]])
    # print(centre)
    t0 = np.array([[t[0] + 0.5], [t[1] + 0.5]])
    # print(t0)
    mat = np.matrix([[0, 1], [-1, 0]])
    # print(mat.T)
    t0 = t0-centre
    # print(t0)
    ts = mat*(t0)+centre
    # print(f'{ts=}')
    ts = (int(ts[0]), int(ts[1]))
    # print(f'Return: {ts}')
    return(ts)
    
t1 = (3,8)
t2 = rot(N,t1)
t3 = rot(N,t2)
t4 = rot(N,t3)
if rot(N,t4) != t1:
    print("Erreur")
t5 = (t1[1],t1[0])
t6 = (t2[1],t2[0])
t7 = (t3[1],t3[0])
t8 = (t4[1],t4[0])

print(t1, x[t1[0]])
print(t2, x[t2[0]])
print(t3, x[t3[0]])
print(t4, x[t4[0]])
print(t5, x[t5[0]])
print(t6, x[t6[0]])
print(t7, x[t7[0]])
print(t8, x[t8[0]])

def nQueen(n):
    N = n
    if N == 1:
        return [0]
    if N == 2 or N == 3:
        return []
    x = [0] * N
    l = []
    for i in range(1,N+1):
        if (i % 2) == 1:
            l.append(i)
        else:
            l.insert(int(i/2)-1,i)
    print(f'{l=}')

    r = N % 6
    if r == 2:
        n = int(N/2)
        a = l[n]
        l[n] = l[n+1]
        l[n+1] = a
        l.remove(5)
        l.append(5)
    print(f'{l=}')

    for i in range(N):
        x[l[i]-1] = i

    print(f'{x=}')
    print_board(N)

    return x

nQueen(21)
