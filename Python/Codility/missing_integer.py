def solution(A):
    s = set(A)
    l = list(s)
    l.sort()
    l.reverse()
    #print(l)
    m = 0
    while l:
        a = l.pop()
        #print(f'a={a}')
        if a > 0:
            if a > m + 1:
                #print(f'end: a={a}, m={m}')
                return m + 1
            else:
                m = a
    if a > 0:
        return a + 1
    return 1

