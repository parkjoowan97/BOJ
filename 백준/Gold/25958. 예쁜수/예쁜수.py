import math
N, K = map(int,input().split())
#K는 소수인 것에 주의하면 될 것 같다

pretty_number = []
for i in range (1, N + 1):
    str_i = str(i)
    n = len(str_i)
    summary = 0
    for j in range (n):
        summary += int(str_i[j])
    if i % summary == 0:
        pretty_number.append(i)

#중복 제거
pretty_number = list(set(pretty_number))
dp = [0 for _ in range (0, N + 1)]

for i in range (0, len(pretty_number)):
    dp[pretty_number[i]] += 1
    for j in range (pretty_number[i] + 1, N + 1):
        dp[j] += dp[j - pretty_number[i]]
print(dp[-1] % K)
