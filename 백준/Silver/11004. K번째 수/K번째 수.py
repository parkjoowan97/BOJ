import sys
input = sys.stdin.readline

N, K = map(int,input().split())
number = list(map(int,input().split()))
number.sort()
print(number[K-1])