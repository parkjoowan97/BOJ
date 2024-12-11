import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    sang_geun = defaultdict(int)
    for _ in range (N):
        sang_geun[int(input())] += 1

    cnt = 0
    for _ in range (M):
        k = int(input())
        if sang_geun[k] == 1:
            cnt += 1
    print(cnt)