def solution(A):
    L = len(A)
    B = set(A)
    if L != len(B):
        return 0
    A.sort()
    A.reverse()
    m = 0
    while A:
        a = A.pop()
        if a > m + 1:
            #print(f'end: a={a}, m={m}')
            return 0
        else:
            m = a
    return 1
