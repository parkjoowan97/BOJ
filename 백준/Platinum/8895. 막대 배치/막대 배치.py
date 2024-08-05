import sys
input = sys.stdin.readline

T = int(input())
for _ in range (0,T):
    n,l,r = map(int,input().split())
    dp = [[[0 for _ in range (0,r+2)] for _ in range (0,l+2)] for _ in range (0,n+2)]
    dp[1][1][1]= 1
    if 3 <= n:
        for i in range (2, n+1):
            for j in range (1, l+1):
                for k in range (1, r+1):
                    dp[i][j][k] += dp[i - 1][j - 1][k]
                    dp[i][j][k] += dp[i - 1][j][k - 1]
                    dp[i][j][k] += dp[i - 1][j][k] * (i - 2)
    elif n == 2:
        dp[2][1][2] = 1
        dp[2][2][1] = 1
    print(dp[n][l][r])