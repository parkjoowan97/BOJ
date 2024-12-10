N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
number = A + B
number.sort()
print(*number)