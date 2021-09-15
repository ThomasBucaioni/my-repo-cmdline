# adapted form https://en.wikipedia.org/wiki/Eight_queens_puzzle#Sample_program

import numpy
i = 0
a = [True] * 8
b = [True] * 16
c = [True] * 15
x = [0] * 8

print(f'{i=}')
print(f'{a=}')
print(f'{b=}')
print(f'{c=}')
print(f'{x=}')

def print_board(i):
    b = numpy.matrix([
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-'],
    ])
    # print(b)
    # for k in range(8):
    #     print(b[k])
    for k in range(8):
        if k <= i:
            for l in range(8):
                b[k,l] = 'x'
                b[l,x[k]] = 'x'
                if k-l >= 0:
                    if x[k]-l >= 0:
                        b[k-l,x[k]-l] = 'x'
                    if x[k]+l <= 7:
                        b[k-l,x[k]+l] = 'x'
                if k+l <= 7:
                    if x[k]+l <= 7:
                        b[k+l,x[k]+l] = 'x'
                    if x[k]-l >= 0:
                        b[k+l,x[k]-l] = 'x'
    for k in range(8):
        if k <= i:
            b[k,x[k]] = 'Q'
    print(b)

def my_try(i):
    print(f'--- Call my_try: {i=}, {x=}')
    string = input(f'Line tested {i=}\n')
    j = -1
    q = False
    while j < 7 and not q:
        j += 1
        print(f'{i=}, {j=}, {i+j=}, {i-j+7=}, a[{j}]={a[j]}, b[{i+j}]={b[i+j]}, c[{i-j+7}]={c[i-j+7]}')
        if a[j] and b[i+j] and c[i-j+7]:
            x[i] = j
            print(f'{x=}')
            print_board(i)
            a[j] = False
            b[i+j] = False
            c[i-j+7] = False
            if i < 7:
                q = my_try(i+1)
                if not q:
                    a[j] = True 
                    b[i+j] = True
                    c[i-j+7] = True
            else:
                q = True
    string = input(f'--- Exits my_try: {q=}\n')
    return q

q = my_try(0)
print(f'Resultat: {q=}')
if q:
    for i in range(8):
        print(x[i])
