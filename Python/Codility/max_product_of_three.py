def solution(A):
    A.sort()
    return A[-1] * A[-2] * A[-3]
