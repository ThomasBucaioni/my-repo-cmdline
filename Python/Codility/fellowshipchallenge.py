def findargmin(S):
    print(S)
    l = len(S)
    m = 27
    I = l
    for i in range(l):
        if S[i] < m:
            m = S[i]
            I = i
    return I

def solution(S, K):
    #print(S, K)
    l = len(S)
    s = []
    #print(S)
    m = 27
    I = l
    for i in range(l):
        x = ord(S[i])-96
        #print(x)
        s.append(x)
        if x < m:
            m = x
            I = i
            #print(f'found smaller letter: {x}, {I}')
    while K>0:
        
        #print(f'K={K}')
        if I != 0:
            c = s[I-1]
            s[I-1] = s[I]
            s[I] = c
            I = I-1
            K = K-1
            #print(f'Case I>0: s={s}')
        else:
            c = s[0]
            r = s[1:]
            t = []
            for j in range(l-1):
                t.append(chr(r[j]+96))
            t = ''.join(t)
            #print(f'new string: {r} = {t}')
            r = solution(t, K)
            z = chr(c+96) + r
            #print(f'final string: {z}')
            return z
            
    t = []
    for j in range(l):
        t.append(chr(s[j]+96))
    #print("To return: ", ''.join(t))
    return ''.join(t)

