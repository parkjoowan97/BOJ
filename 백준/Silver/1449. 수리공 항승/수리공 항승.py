import sys
input = sys.stdin.readline
N,L = map(int,input().split())
spot = list(map(int,input().split()))
spot.sort()
cnt = 1
length = spot[0] - 0.5
for i in range (0,N):
    if length <= spot[i] <= length + L:
        continue
    else:
        cnt += 1
        length = spot[i] - 0.5
print(cnt)