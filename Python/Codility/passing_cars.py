def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    #print(f'{P=}')
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]

def solution(A):
    pref = prefix_sums(A)
    l = len(A)
    n = 0
    for i in range(l):
        if A[i] == 0:
            n += pref[l] - pref[i]
            if n > 1_000_000_000:
                return -1
    return n

