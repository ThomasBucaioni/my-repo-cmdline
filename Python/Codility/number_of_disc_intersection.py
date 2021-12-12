#!/bin/python3

A = [1,5,2,1,4,0]

l = len(A)

T = []
for i in range(len(A)):
    T.append((i,A[i]))

B = sorted(T, key=lambda tup: tup[1])

print(f"{A=}\n{T=}\n{B=}")

B.reverse()

nbrectot = 0

for i in range(l):
    t = B[i]
    print(f"{t=}\t")
    nbrec = max(0,t[0]-t[1])
    nbv = t[0] - nbrec
    nbrec = min(l,t[0]+t[1])
    nbv += nbrec - t[0]
    nbrectot += nbv
    print(f"{nbrectot=}")
    if i < l-1:
        lim = B[i+1][1]
        print(f"{lim=}")
        for j in range(1,lim):
            if t[0] + j < l:
                u = t[0] + j
                print(f"{u=}, {A[u]=}")
                if A[u] > j:
                    nbrectot += 1

    print(f"{nbrectot=}")
print(f"{nbrectot=}")
