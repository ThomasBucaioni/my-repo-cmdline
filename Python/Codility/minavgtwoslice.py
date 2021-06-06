def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

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
    print(f'slice: {i=}, {j=}, {m=}, {A[i:j+1]}')
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
def solution3(A): # test faster algo
    I = i = 0
    J = j = 1
    memm = sum(A[i:j+1])/(j+1-i)
    l = len(A)
    while i < l-1 and j < l:
        #print(f"entrance: {i=}, {j=}, {memm=}")
        #print('-')
        m = sum(A[i:j+1])/(j+1-i)
        if m < memm:
            #print(f'better mean found: {A[i:j+1]=}, {m=}')
            I = i
            J = j
            memm = m
        #else: print('no better mean')
        #print('-')
        #print(f'cleaning loop: test if {i}<{j-1} -> {i<j-1}')
        if i < j-1:
            b = False
            #print('-')
            for k in range(i+1,j):
                #print(f'cleaning loop: {k=} in [{i+1}, {j-1}]')
                mb = sum(A[k:j+1])/(j+1-k)
                #print(f"mean with elements before {k-1} removed : {mb=}")
                if m > mb:
                    #print(f'removing elements in the slice: next i={k}')
                    i = k
                    b = True
            #print('-')
            if b == True:
                #print('continue the while loop')
                #print(f"exit: {i=}, {j=}, {A[i:j+1]=}, {memm=}, {I=}, {J=}, {A[I:J+1]=}")
                #input('stop')
                #print('--')
                continue
        #print('-')
        if j < l:
            mb = sum(A[i:j+2])/(j+2-i)
            #print(f"next mean: {mb=}")
            if mb > m:
                #print(f'restart from i={j+1}')
                i = j+1
                j = j+2
            else:
                j += 1
                #print('increasing the slice')
        #print('-')        
        #print(f"exit: {i=}, {j=}, {A[i:j+1]=}, {memm=}, {I=}, {J=}, {A[I:J+1]=}")
        #input('stop')
        #print('--')
    print(f"slice: {I=}, {J=}, m={memm}, {A[I:J+1]}")

solution3(A)

print('-----')
print('-----')
for t in range(10):
    A = [random.randint(1,10) for i in range(20)]
    print(A)
    solution1(A)
    solution3(A)
    print('-----')

A=[10, 6, 8, 5, 9, 10, 1, 7, 9, 3, 9, 9, 4, 7, 1, 8, 6, 10, 9, 4]
