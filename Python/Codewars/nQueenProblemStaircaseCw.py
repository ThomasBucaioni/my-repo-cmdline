import numpy as np

N=21

def print_board(i,x):
    print(N,x)
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

def nQueen(N):
    if N == 1:
        return [0]
    if N == 2 or N == 3:
        return []
    global x
    x = [0] * N
    l = []
    for i in range(1,N+1):
        if (i % 2) == 1:
            l.append(i)
        else:
            l.insert(int(i/2)-1,i)
    print(f'{l=}')

    r = N % 6
    print(r)
    if r == 2:
        n = int(N/2)
        a = l[n]
        l[n] = l[n+1]
        l[n+1] = a
        l.remove(5)
        l.append(5)
    elif r == 3:
        l.remove(2)
        l.insert(int(N/2),2)
        l.remove(1)
        l.remove(3)
        l.append(1)
        l.append(3)
    print(f'{l=}')

    for i in range(N):
        x[l[i]-1] = i

    print(f'{x=}')
    print_board(N,x)

    return x

nQueen(21)
