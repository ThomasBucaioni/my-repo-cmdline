# [5, 6, 3, 4, 9]
# [-1, -10, 0, -500, -1, 0, 1]
# [-3, -5, -8, -4, -10]

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def solution(A):
    n = len(A)
    result = 0
    pref = prefix_sums(A)
    i = 0
    m = sum([a for a in A if a>0])
    for p in range(n-1):
        for q in range(p+1,n):
            r = count_total(pref,p,q)/(q-p+1)
            if r<m:
                m = r
                i = p
    return i

def solution(A):
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
    m = sum([a for a in A if a>0])
    for p in range(n-1):
        for q in range(p+1,min(p+L,n)):
            r = count_total(pref,p,q)/(q-p+1)
            if r<m:
                m = r
                i = p
    #print(f'Min slice: {m}')
    return i
