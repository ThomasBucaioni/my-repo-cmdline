# adapted form https://en.wikipedia.org/wiki/Eight_queens_puzzle#Sample_program

import numpy as np
N = 8
a = [True] * N
b = [True] * 2 * N
c = [True] * ( 2 * N - 1 )
x = [0] * N

fi = 1
fj = 0
x[fi] = fj
a[fj] = False
b[fi+fj] = False
c[fi-fj+(N-1)] = False

print(f'{i=}')
print(f'{a=}')
print(f'{b=}')
print(f'{c=}')
print(f'{x=}')

def print_board(i):
    #print(N)
    b = numpy.zeros((N,N),dtype=np.str)
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

def my_try(i):
    print(f'--- Call my_try: {i=}, {x=}')
    string = input(f'Line tested {i=}\n')
    j = -1
    q = False
    if fi == i:
        q = my_try(i+1)
    else:
        while j < N-1 and not q:
            j += 1
            print(f'{i=}, {j=}, {i+j=}, {i-j+N-1=}, a[{j}]={a[j]}, b[{i+j}]={b[i+j]}, c[{i-j+N-1}]={c[i-j+N-1]}')
            if a[j] and b[i+j] and c[i-j+N-1]:
                x[i] = j
                print(f'{x=}')
                print_board(i)
                a[j] = False
                b[i+j] = False
                c[i-j+N-1] = False
                if i < N-1:
                    q = my_try(i+1)
                    if not q:
                        a[j] = True 
                        b[i+j] = True
                        c[i-j+N-1] = True
                else:
                    q = True
    string = input(f'--- Exits my_try: {q=}\n')
    return q

if fi == 0:
    q = my_try(1)
else:
    q = my_try(0)
print(f'Resultat: {q=}')
if q:
    for i in range(N):
        print(x[i])
    print_board(N-1)
