def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    #print(f'{P=}')
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def my_count_total(P, x, y):
    #print(len(P),x,y)
    return P[y-1] - P[x-1]

def solution1(A):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    i = 0
    j = 1
    m = sum([a for a in A if a>0])
    for p in range(n-1):
        for q in range(p+1,n):
            r = count_total(pref,p,q)/(q-p+1)
            if r<m:
                m = r
                i = p
                j = q
    #print(f'slice: {i=}, {j=}, {m=}, {A[i:j+1]}')
    return i

def solution2(A):
    n = len(A)
    L = 1
    l = 1
    e = A[0]
    for i in range(1,n):
        if A[i] != e:
            e = A[i]
            l = 1
        else:
            l += 1
            if L < l:
                L = l
    #print(f'Max ids: {L}')
    result = 0
    pref = prefix_sums(A)
    i = 0
    j = 0
    m = sum([a for a in A if a>0])
    for p in range(n-1):
        for q in range(p+1,min(p+L,n)):
            r = count_total(pref,p,q)/(q-p+1)
            if r<m:
                m = r
                i = p
                j = q
    #print(f'Min slice: {m}')
    print(f'slice: {i=}, {j=}, {m=}')
    return i

A = [5, 6, 3, 4, 9]
print(A)
solution1(A)
solution2(A)

A = [-1, -10, 0, -500, -1, 0, 1]
print(A)
solution1(A)
solution2(A)

A = [-3, -5, -8, -4, -10]
print(A)
solution1(A)
solution2(A)

import random
random.seed(1)
A = [random.randint(1,10) for i in range(20)]
print(A)
solution1(A)

print('-----')
print(f'{A=}')
print('---')
def solution3debug(A): # test faster algo
    I = i = 0
    J = j = 1
    memm = sum(A[i:j+1])/(j+1-i)
    l = len(A)
    pref = prefix_sums(A)
    while i < l-1 and j < l:
        print(f"entrance: {i=}, {j=}, {memm=}")
        print('-')
        m = sum(A[i:j+1])/(j+1-i)
        if m < memm:
            print(f'better mean found: {A[i:j+1]=}, {m=}')
            I = i
            J = j
            memm = m
        else: print('no better mean')
        print('-')
        print(f'cleaning loop: test if {i}<{j-1} -> {i<j-1}')
        if i < j-1:
            b = False
            print('-')
            for k in range(i+1,j):
                print(f'cleaning loop: {k=} in [{i+1}, {j-1}]')
                mb = sum(A[k:j+1])/(j+1-k)
                print(f"mean with elements before {k-1} removed : {mb=}")
                if m > mb:
                    print(f'removing elements in the slice: next i={k}')
                    i = k
                    b = True
            print('-')
            if b == True:
                print('continue the while loop')
                print(f"exit: {i=}, {j=}, {A[i:j+1]=}, {memm=}, {I=}, {J=}, {A[I:J+1]=}")
                input('stop')
                print('--')
                continue
        print('-')
        if j < l:
            mb = sum(A[i:j+2])/(j+2-i)
            print(f"next mean: {mb=}")
            if mb > m:
                print(f'restart from i={j}')
                i = j
                j = j+1
            else:
                j += 1
                print('increasing the slice')
        print('-')        
        print(f"exit: {i=}, {j=}, {A[i:j+1]=}, {memm=}, {I=}, {J=}, {A[I:J+1]=}")
        input('stop')
        print('--')
    print(f"slice: {I=}, {J=}, m={memm}, {A[I:J+1]}")

# solution3(A)

# print('-----')
# print('-----')
# for t in range(10):
#     A = [random.randint(1,10) for i in range(20)]
#     print(A)
#     solution1(A)
#     solution3(A)
#     print('-----')

def solution3(A): # test faster algo
    Mmin = min(A)
    Mmax = max(A)
    if Mmin == Mmax:
        return 0
    pref = prefix_sums(A)
    I = i = 0
    J = j = 1
    memm = count_total(pref,i,j)/(j+1-i)#sum(A[i:j+1])/(j+1-i)
    l = len(A)
    while i < l-1 and j < l:
        m = count_total(pref,i,j)/(j+1-i)#sum(A[i:j+1])/(j+1-i)
        if m < memm:
            I = i
            J = j
            memm = m
            if memm == Mmin:
                return I
        if i < j-1:
            b = False
            for k in range(i+1,j):
                mb = count_total(pref,k,j)/(j+1-k)#sum(A[k:j+1])/(j+1-k)
                if m > mb:
                    i = k
                    b = True
            if b == True:
                continue
        if j < l:
            #print(i,j+1)
            mb = count_total(pref,i,min(j+1,l-1))/(j+2-i)#sum(A[i:j+2])/(j+2-i)
            if mb > m:
                i = j
                j = j+1
            else:
                j += 1
    #print(f"slice: {I=}, {J=}, m={memm}, {A[I:J+1]}")
    return I

A=[10, 6, 8, 5, 9, 10, 1, 7, 9, 3, 9, 9, 4, 7, 1, 8, 6, 10, 9, 4]
print(f'{A=}')
solution1(A)
solution3(A)

import time
print(time.time())
random.seed(time.time())
#random.seed(1)
cmpt = 0
while True:
    cmpt += 1
    A = [random.randint(1,10) for i in range(5)]
    a = solution1(A)
    b = solution3(A)
    #if cmpt == 15: b = 6
    if a != b:
        print('BUG', A)
        exit(1)
    A = [random.randint(-1,1) for i in range(100000)]
    #print(A)
    t01 = time.time()
    #a = solution1(A)
    t02 = time.time()
    b = solution3(A)
    t03 = time.time()
    #print(t02-t01,t03-t02)
    # if a != b:
    #     print('BUG', A)
    #     exit(1)
    A = [random.randint(1,10) for i in range(20)]
    t11 = time.time_ns()
    a = solution1(A)
    t12 = time.time_ns()
    b = solution3(A)
    t13 = time.time_ns()
    if a != b:
        print('BUG', A)
        exit(1)
    A = [random.randint(1,10) for i in range(100)]
    t21 = time.time_ns()
    a = solution1(A)
    t22 = time.time_ns()
    b = solution3(A)
    t23 = time.time_ns()
    if a != b:
        print('BUG', A)
        exit(1)
    A = [random.randint(1,100) for i in range(100)]
    t31 = time.time_ns()
    a = solution1(A)
    t32 = time.time_ns()
    b = solution3(A)
    t33 = time.time_ns()
    if a != b:
        print('BUG', A)
        exit(1)
    A = [random.randint(1,50) for i in range(1000)]
    t41 = time.time_ns()
    a = solution1(A)
    t42 = time.time_ns()
    b = solution3(A)
    t43 = time.time_ns()
    if a != b:
        print('BUG', A)
        exit(1)
    print(f'{cmpt=}, \
    dt11={100*((t13-t12)-(t12-t11))/(t12-t11):+8.2f}%, \
    dt21={100*((t23-t22)-(t22-t21))/(t22-t21):+8.2f}%, \
    dt31={100*((t33-t32)-(t32-t31))/(t32-t31):+8.2f}%, \
    dt41={100*((t43-t42)-(t42-t41))/(t42-t41):+8.2f}%')

#-----
A = [3, 7, 3, 7, 1]
A = [-3, -5, -8, -4, -10]
print('-----')
print(f'{A=}')
print('---')
solution1(A)
#solution3debug(A)
solution3(A)
