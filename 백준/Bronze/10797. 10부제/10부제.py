n = int(input())
num = list(map(int,input().split()))
cnt = 0
for a in num:
    if a == n:
        cnt += 1
print(cnt)