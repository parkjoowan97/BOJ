import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
for i in range(1, N+1):
    for j in range(i, N+1):
        k = N-i-j
        if k >= i + j:
            continue
        else:
            if j > k:
                break
            cnt += 1
print(cnt)