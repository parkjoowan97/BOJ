import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int,input().split()))

mix_val = int(1e9) * 2
ans_l, ans_r = 0, N-1

l, r = 0, N-1
while l < r:
    val = liquid[l] + liquid[r]
    if abs(val) < mix_val:
        ans_l, ans_r = l, r
        mix_val = abs(val)
        if val == 0:
            break
    if val <= 0:
        l += 1
    else:
        r -= 1
print(liquid[ans_l], liquid[ans_r])