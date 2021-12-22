#!/bin/python3

A = [1,5,2,1,4,0]

l = len(A)
print(f"Array length: {l=}")

T = []
for i in range(len(A)):
    T.append((i,A[i]))

B = sorted(T, key=lambda tup: (tup[1],tup[0]))

print(f"{A=}\n{T=}\n{B=}")

B.reverse()

nbdrectot = 0
nbsrectot = 0

for i in range(l):
    t = B[i]
    print('----------')
    print(f"Biggest circle: {t=}\t")

    # Covered points below
    nbrec = t[0] - max(0,t[0]-t[1]) # number of overlapped points below
    print(f"Number of overlapped points below: {nbrec=}\t")
    nbv = 0
    for j in range(nbrec):
        u = t[0] - j - 1
        if A[u] < t[1]:
            nbv += 1
            print(f"Overlap, strict: p={(u,A[u])}, {t=}")
        elif A[u] == t[1] and u < t[0]:
            nbv += 1
            print(f"Overlap, equal: {(u,A[u])}, {t=}")
    nbdrectot += nbv

    # Covered points above
    nbrec = min(l-1,t[0]+t[1]) - t[0] # number of overlapped points above
    print(f"Number of overlapped points above: {nbrec=}\t")
    nbv = 0
    for j in range(nbrec):
        u = t[0] + j + 1
        if A[u] < t[1]:
            nbv += 1
            print(f"Overlap, strict: p={(u,A[u])}, {t=}")
        elif A[u] == t[1] and u > t[0]:
            nbv += 1
            print(f"Overlap, equal: {(u,A[u])}, {t=}")
    nbdrectot += nbv
    
    print(f"Number of point overlaps so far: {nbdrectot=}")
    print('-----')

    if i < l-1:
        lim = B[i+1][1]
        print(f"Limit of neighbors to parse: {lim=}")
        for j in range(1,lim):
            if t[0] + j < l:
                u = t[0] + j
                print(f"Maybe new intersection: {u=}, {A[u]=}, {j=}")
                if abs(u-t[0])>t[1] and A[u] > j:
                    print('\tNew intersection')
                    nbsrectot += 1
            elif t[0] - j >= 0:
                u = t[0] - j
                print(f"Maybe new intersection: {u=}, {A[u]=}, {j=}")
                if abs(u-t[0])>t[1] and A[u] > j:
                    print('\tNew intersection')
                    nbsrectot += 1
                    
    print(f"Number of disk overlaps so far: {nbsrectot=}")
            
    print(f"{nbdrectot=}, {nbsrectot=}")
print(f"{nbdrectot=}, {nbsrectot=}, tot: {nbdrectot+nbsrectot}")
