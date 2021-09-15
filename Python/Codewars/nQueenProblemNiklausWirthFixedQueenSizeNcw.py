import numpy as np

def print_board(i):
    #print(N)
    b = np.zeros((N,N),dtype=np.str)
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
    #print(f'--- Call my_try: {i=}, {x=}')
    #string = input(f'Line tested {i=}\n')
    j = -1
    q = False
    if fi == i:
        q = my_try(i+1)
    else:
        while j < N-1 and not q:
            j += 1
            #print(f'{i=}, {j=}, {i+j=}, {i-j+N-1=}')
            #print(f'a[{j}]={a[j]}, b[{i+j}]={b[i+j]}, c[{i-j+N-1}]={c[i-j+N-1]}')
            if a[j] and b[i+j] and c[i-j+N-1]:
                x[i] = j
                #print(f'{x=}')
                #print_board(i)
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
    #string = input(f'--- Exits my_try: {q=}\n')
    return q

def solve_n_queens(n, fixed_queen):
    global N
    N = n
    global x
    x = [0] * N
    if n == 1:
        return 'Q\n'
    elif n <=8:
        global fi
        fi = fixed_queen[0]
        global fj
        fj = fixed_queen[1]
        global a
        a = [True] * N
        global b
        b = [True] * 2 * N
        global c
        c = [True] * ( 2 * N - 1 )

        print(f'{N=}')
        #print(f'{a=}')
        #print(f'{b=}')
        #print(f'{c=}')
        #print(f'{x=}')

        x[fi] = fj
        a[fj] = False
        b[fi+fj] = False
        c[fi-fj+(N-1)] = False

        if fi == 0:
            q = my_try(1)
        else:
            q = my_try(0)

        #print(f'Result: {q=}')
        if q:
            s = ''
            for i in range(N):
                #print(x[i])
                s = s + '.' * x[i] + 'Q' + '.' * ( N - x[i] - 1 ) + '\n'
            #print(f'{s=}')
            return s
        else:
            return None
    else:
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

        s = ''
            for i in range(N):
            #print(x[i])
            s = s + '.' * x[i] + 'Q' + '.' * ( N - x[i] - 1 ) + '\n'
        #print(f'{s=}')
        return s


