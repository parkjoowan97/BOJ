N = int(input())
mod = 1_000_000_000
#길이가 N이면서 0부터 9까지 나오려면... 최소 길이는 10
num_range = 10
bit_range = 1 << num_range
DP = [[[0] * (bit_range) for _ in range(num_range)] for _ in range (N+1)]

for k in range (num_range):
    DP[1][k][1<<k] = 1

for i in range(1, N):
    for j in range (num_range):
        for b in range (bit_range):
            if 0 <= j < 9:
                more = b | 1<<(j+1)
                DP[i+1][j+1][more] += DP[i][j][b]
                DP[i+1][j+1][more] %= mod
            if 0 < j <= 9:
                less = b | 1<<(j-1)
                DP[i+1][j-1][less] += DP[i][j][b]
                DP[i+1][j-1][less] %= mod

answer = 0
for k in range(1,num_range):
    answer += DP[N][k][0b1111111111]
print(answer % mod)