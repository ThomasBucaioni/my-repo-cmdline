def solution(S, P, Q):
    Lpq = len(P)
    sol = []
    for j in range(Lpq):
        p = P[j]
        q = Q[j]
        s = S[p:q+1]
        if 'A' in s:
            sol.append(1)
        elif 'C' in s:
            sol.append(2)
        elif 'G' in s:
            sol.append(3)
        else:
            sol.append(4)
    return sol
