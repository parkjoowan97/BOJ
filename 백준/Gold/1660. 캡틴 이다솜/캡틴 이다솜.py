import sys
input = sys.stdin.readline

N = int(input())
bullet, bullet_sum = [1], [1]
cnt = 2

while bullet_sum[-1] <= N:
    bullet.append((cnt * (cnt + 1)) // 2)
    bullet_sum.append(bullet_sum[-1] + bullet[-1])
    cnt += 1

dp = [N for _ in range (0, N + 1)]

for i in range (0, len(bullet_sum)-1):
    dp[bullet_sum[i]] = 1
    for j in range (bullet_sum[i] + 1, N + 1):
        dp[j] = min(dp[j - bullet_sum[i]] + 1, dp[j])

print(dp[-1])