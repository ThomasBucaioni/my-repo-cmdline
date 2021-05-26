# A = 11, B = 345, K = 17
# A = B in {0,1}, K = 11
# A = 10, B = 10, K in {5,7,20}
# A = 0, B = MAXINT, K in {1,MAXINT}
# A, B, K in {1,MAXINT}

def solution(A, B, K):
    r0 = A%K
    if r0 == 0:
        A0 = A
    else:
        A0 = A + K - r0
    #print(f'A0={A0}, r={A0 % K}')
    if A0 > B:
        return 0
    r0 = B%K
    if r0 == 0:
        B0 = B
    else:
        B0 = B - r0
    #print(f'B0={B0}, r={B0 % K}')
    if A0 == B0:
        return 1
    else:
        return (B0 - A0)//K + 1
