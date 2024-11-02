A, K = map(int,input().split())
cnt = 0
while A <= K // 2:
    cnt += 1 + (K & 1)
    K = K // 2
print(cnt + K - A)