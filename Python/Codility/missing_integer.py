import numpy as np
def solution(A):
    L = len(A)
    A.sort()
    s = set(A)
    l = list(s)
    l.sort()
    print(l)
    m = l.pop()
    M = m
    if m <= 0:
        return 1
    if m == 1:
        return 2
    if not l:
        return m - 1
    while l:
        a = l.pop()
        if a <= 1:
            if a == 1:
                if m == 3:
                    return 2
                else:
                    return M + 1
            else:
                return 1
        if a < m - 1:
            return m - 1
        else:
            m = a
    print('Bug')    

A = list(range(10))
A = np.random.randint(0,100,600)
A = [4, 5, 6, 2]
s = solution(A)
print(s)
