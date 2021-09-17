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
    
def my_try(i):
    #print(f'--- Call my_try: {i=}, {x=}')
    #string = input(f'Line tested {i=}\n')
    j = -1
    q = False
    if fi == i:
        if i == N-1:
            print('ok')
            return True
        else:
            q = my_try(i+1)
    else:
        while j < N-1 and not q:
            j += 1
            #print(f'{i=}, {j=}, {i+j=}, {i-j+N-1=}')
            #print(f'a[{j}]={a[j]}, b[{i+j}]={b[i+j]}, c[{i-j+N-1}]={c[i-j+N-1]}')
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
    #string = input(f'--- Exits my_try: {q=}\n')
    return q



def queens(position, size):
    print(f'{position=}, {size=}')
    global N
    N = size
    global x
    x = [0] * N
    if size == 1:
        return 'a1'
    elif size <=10:
        global fi
        fi = ord(position[0])-97
        global fj
        if int(position[1]) == 0:
            fj = 9
        else:
            fj = int(position[1])-1
        global a
        a = [True] * N
        global b
        b = [True] * 2 * N
        global c
        c = [True] * ( 2 * N - 1 )

        print(f'{N=}')
        print(f'{a=}')
        print(f'{b=}')
        print(f'{c=}')
        print(f'{x=}')
        
        print(f'{fi=}')
        print(f'{fj=}')

        x[fi] = fj
        a[fj] = False
        b[fi+fj] = False
        c[fi-fj+(N-1)] = False

        q = my_try(0)

        print(f'Result: {q=}')
        if q:
            s = ''
            for i in range(size):
                s = s + chr(i+97) + str(x[i]+1) + ','
            #for i in range(N):
                #print(x[i])
                #s = s + '.' * x[i] + 'Q' + '.' * ( N - x[i] - 1 ) + '\n'
            print(f'{s[0:-1]=}, {type(s)}')
            return s[0:-1]
        else:
            return None
    return "a1,b2,c3,d4,e5,f6,g7,h8,i9,j0"

queens('b0',10)
