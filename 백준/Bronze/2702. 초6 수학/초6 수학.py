import math
t = int(input())
for _ in range (0,t):
    a,b =  map(int,input().split())
    print(math.lcm(a,b),math.gcd(a,b))