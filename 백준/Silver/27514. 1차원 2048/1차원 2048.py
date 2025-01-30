import sys
import math

N = int(input())
num = list(map(int,input().split()))
binary_num = [0 for _ in range (0, 100)]

for number in num:
    if number != 0:
        binary_num[int(math.log2(number))] += 1


for i in range (0, 99):
    binary_num[i+1] += (binary_num[i] // 2)

for i in range (99, -1, -1):
    if binary_num[i] == 1:
        print(2 ** i)
        break
