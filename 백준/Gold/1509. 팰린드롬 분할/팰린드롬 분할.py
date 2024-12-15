import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

pal = [[False]*n for _ in range(n)]

for i in range(n):
    pal[i][i] = True

for length in range(2, n+1):
    for start in range(n-length+1):
        end = start + length - 1
        if s[start] == s[end]:
            if length == 2 or pal[start+1][end-1]:
                pal[start][end] = True

dp = [0]*n
for i in range(n):
    if pal[0][i]:
        dp[i] = 1
    else:
        dp[i] = float('inf')
        for j in range(1, i+1):
            if pal[j][i] and dp[j-1] + 1 < dp[i]:
                dp[i] = dp[j-1] + 1

print(dp[n-1])