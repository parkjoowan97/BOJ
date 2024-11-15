N = int(input())

files = list(map(int,input().split()))

K = int(input())
cnt = 0
for i in range (0, len(files)):
    if files[i] % K == 0:
        cnt += (files[i] // K)
    else:
        cnt += (files[i] // K) + 1

print(cnt * K)