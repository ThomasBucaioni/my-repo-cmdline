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
