#!/bin/python3

def solution(A):

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
            if A[u] <= t[1]:
                nbv += 1
                print(f"Overlap, strict: p={(u,A[u])}, {t=}")
            #elif A[u] == t[1] and u < t[0]:
            #    nbv += 1
            #    print(f"Overlap, equal: {(u,A[u])}, {t=}")
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
            #elif A[u] == t[1] and u > t[0]:
            #    nbv += 1
            #    print(f"Overlap, equal: {(u,A[u])}, {t=}")
        nbdrectot += nbv

        print(f"Number of point overlaps so far: {nbdrectot=}")
        print('-----')

        if i < l-1:
            lim = B[i+1][1]
            print(f"Limit of neighbors to parse: {lim}")
            for j in range(0,lim):
                if t[0] + t[1] + j + 1 < l:
                    u = t[0] + t[1] + j
                    print(f"Maybe new intersection: {u=}, {A[u]=}, {j=}")
                    if abs(u-t[0]) < (t[1]+A[u]) and A[u] < t[1]:
                        print('\tNew intersection')
                        nbsrectot += 1
                elif t[0] - t[1] - j - 1 >= 0:
                    u = t[0] - t[1] - j
                    print(f"Maybe new intersection: {u=}, {A[u]=}, {j=}")
                    if abs(u-t[0]) < (t[1]+A[u]):
                        print('\tNew intersection')
                        nbsrectot += 1

        print(f"Number of disk overlaps so far: {nbsrectot=}")

        print(f"{nbdrectot=}, {nbsrectot=}")
    print(f"{nbdrectot=}, {nbsrectot=}, tot: {nbdrectot+nbsrectot}")

#exit(0)

def solution(A):

    l = len(A)

    T = []
    for i in range(len(A)):
        T.append((i,A[i]))

    B = sorted(T, key=lambda tup: (tup[1],tup[0]))

    B.reverse()

    nbdrectot = 0
    nbsrectot = 0

    for i in range(l):
        t = B[i]

        # Covered points below
        nbrec = t[0] - max(0,t[0]-t[1]) # number of overlapped points below
        nbv = 0
        for j in range(nbrec):
            u = t[0] - j - 1
            if A[u] <= t[1]:
                nbv += 1
        nbdrectot += nbv

        # Covered points above
        nbrec = min(l-1,t[0]+t[1]) - t[0] # number of overlapped points above
        nbv = 0
        for j in range(nbrec):
            u = t[0] + j + 1
            if A[u] < t[1]:
                nbv += 1
        nbdrectot += nbv

        if i < l-1:
            lim = B[i+1][1]
            for j in range(0,lim):
                if t[0] + t[1] + j + 1 < l:
                    u = t[0] + t[1] + j
                    if abs(u-t[0]) < (t[1]+A[u]) and A[u] < t[1]:
                        nbsrectot += 1
                elif t[0] - t[1] - j - 1 >= 0:
                    u = t[0] - t[1] - j
                    if abs(u-t[0]) < (t[1]+A[u]):
                        nbsrectot += 1

    return nbdrectot+nbsrectot

def solutionref(A):

    l = len(A)

    T = []
    for i in range(len(A)):
        T.append((i,A[i]))

    B = sorted(T, key=lambda tup: (tup[1],tup[0]))

    B.reverse()

    print(f"{B}")
    
    n = 0
    
    for i in range(l):
        for j in range(i+1,l):
            if abs(B[i][0] - B[j][0]) <= B[i][1] + B[j][1]:
                n +=1
            #else:
            #    break
    print(f"Sol ref: {n=}")
    return n

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG)

def solution(A):

    l = len(A)

    T = []
    for i in range(len(A)):
        T.append((i,A[i]))

    B = sorted(T, key=lambda tup: (tup[1],tup[0]))

    B.reverse()

    logging.debug('----------')
    logging.debug(f"{A}")
    logging.debug('----------')
    logging.debug(f"{B}")
    
    n = 0
    
    for i in range(l):
        logging.debug('----------')
        p = B[i][0]
        r = B[i][1]
        logging.debug(f"{p=}, {r=}, M={min(p+r+1, l)}, m={max(p-r-1, 0)}")
        for j in range(p+1, min(p+r+1, l)):
            logging.debug(f"\t{j=}", end='')
            if j - p > A[j]:
                n += 1
                logging.debug(f", overlap: {n=}")
            elif A[j] < A[p]:
                n += 1
                logging.debug(f", overlap: {n=}")
            elif A[j] == A[p] and p > j:
                n += 1
                logging.debug(f", overlap: {n=}")
            else:
                logging.debug('')
        for j in range(max(p-r, 0), p):
            logging.debug(f"\t{j=}", end='')
            if p - j > A[j]:
                n += 1
                logging.debug(f", overlap: {n=}")
            elif A[j] < A[p]:
                n += 1
                logging.debug(f", overlap: {n=}")
            elif A[j] == A[p] and p > j:
                n += 1
                logging.debug(f", overlap: {n=}")
            else:
                logging.debug('')
        if i < l-1:
            s = B[i+1][1]
            logging.debug(f"pp={B[i+1][0]},rp={s}")
            for j in range(p+r+1, min(p+r+s+1, l)):
                logging.debug(f"\t{j=}")
                if j - p <= r + A[j] and (A[j] < r or (A[j] == r and p > j)):
                    n += 1
                    logging.debug(f"\t\toverlap: {n=}")
            for j in range(max(p-r-s-1, 0), p-r):
                logging.debug(f"\t{j=}")
                if p - j <= r + A[j] and (A[j] < r or (A[j] == r and p > j)):
                    n += 1
                    logging.debug(f"\t\toverlap: {n=}")
        logging.debug(f"{n=}")
        #input("Press Enter to continue...")
    logging.debug(f"{n=}")
    #input("Press Enter to continue...")
    return n

#if (False):
if (True):
    A = [1, 2, 0, 1, 1, 2]
    print('>>>>>> ', solutionref(A) == solution(A), ' <<<<<<\n')
    A = [1,5,2,1,4,0]
    print('>>>>>> ', solutionref(A) == solution(A), ' <<<<<<\n')
    A = [1,1,1]
    print('>>>>>> ', solutionref(A) == solution(A), ' <<<<<<\n')
    A = [1, 10, 100, 1]
    print('>>>>>> ', solutionref(A) == solution(A), ' <<<<<<\n')
    A = [1, 0, 1, 0, 1]
    print('>>>>>> ', solutionref(A) == solution(A), ' <<<<<<\n')

import random
N = 20
A = [0] * N
for i in range(N):
    for j in range(N):
        A[j] = random.randint(0,N)
    print('>>>>>> ', solutionref(A) == solution(A), ' <<<<<<\n')
    input("Press Enter to continue...")
    



def solutionOkButTimeOut(A):

    l = len(A)

    T = []
    for i in range(len(A)):
        T.append((i,A[i]))

    B = sorted(T, key=lambda tup: (tup[1],tup[0]))

    B.reverse()

    n = 0
    
    for i in range(l):
        p = B[i][0]
        r = B[i][1]
        for j in range(p+1, min(p+r+1, l)):
            if j - p > A[j]:
                n += 1
            elif A[j] < A[p]:
                n += 1
            elif A[j] == A[p] and p > j:
                n += 1

        for j in range(max(p-r, 0), p):
            if p - j > A[j]:
                n += 1
            elif A[j] < A[p]:
                n += 1
            elif A[j] == A[p] and p > j:
                n += 1

        if i < l-1:
            s = B[i+1][1]
            for j in range(p+r+1, min(p+r+s+1, l)):
                if j - p <= r + A[j] and (A[j] < r or (A[j] == r and p > j)):
                    n += 1
            for j in range(max(p-r-s-1, 0), p-r):
                if p - j <= r + A[j] and (A[j] < r or (A[j] == r and p > j)):
                    n += 1
    return n

