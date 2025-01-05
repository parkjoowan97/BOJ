import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range (N):
    arr.append(int(input()))

cnt = 0
max_a = 0

for a in reversed(arr):
    if max_a < a:
        cnt += 1
        max_a = a
print(cnt)