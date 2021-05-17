def solution(A):
    print(f"In func: {A}")
    A=set(A)
    A=list(A)
    A.sort()
    print(f"Processing: {A}")
    mmax = A.pop()
    if mmax <= 0:
        print(1)
        return 1
    else:
        Mmax = mmax + 1
        while A:
            a = A.pop()
            if a < mmax - 1:
                print(mmax-1)
                return mmax - 1
            else:
                mmax = a
        print(Mmax)
        return Mmax

import random
random.seed(1)
A = []
A.append(0)
print(A)
print(type(A))
for i in range(1,100):
    print(A)
    a = random.randrange(1,40000)
    A.append(a)
    print(A)
A = [a - 20_000 for a in A]
print(A)

solution(A)

A = list(range(100))
print(A)
random.shuffle(A)
print(A)
solution(A)
