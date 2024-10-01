import sys
import math
input = sys.stdin.readline

def count(A):
    cnt = 0
    divisors = set()
    for i in range(1, int(math.isqrt(A**2)) + 1):
        if (A ** 2) % i == 0:
            divisors.add(i)

    for n in divisors:
        m = (A ** 2) // n
        if (m + n) % 2 == (m - n) % 2 and (m - n) % 2 == 0 and (m - n) // 2 > A:
            cnt += 1
    return cnt

while True:
    a = int(input())
    if a == 0:
        break
    print(count(a))