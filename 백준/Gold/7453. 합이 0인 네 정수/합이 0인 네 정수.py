from collections import defaultdict
import sys
def input():
    return sys.stdin.readline()
N = int(input())

A, B, C, D = [], [], [], []

for _ in range (0, N):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
def f(A, B, C, D):
    AB_sum = defaultdict(int)
    for a in A:
        for b in B:
            AB_sum[a + b] += 1

    cnt = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in AB_sum:
                cnt += AB_sum[target]
    return cnt
print(f(A, B, C, D))