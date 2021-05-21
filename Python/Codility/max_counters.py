def solution(N, A):
    m = 0
    M = 0
    C = []
    for i in range(N):
        C.append(0)
    A.reverse()
    while A:
        a = A.pop()-1
        if a == N:
            m = M
        else:
            if C[a] < m:
                C[a] = m + 1
            else:
                C[a] = C[a] + 1
            if C[a] > M:
                M = C[a]
    for i in range(N):
        if C[i] < m:
            C[i] = m
    return C
