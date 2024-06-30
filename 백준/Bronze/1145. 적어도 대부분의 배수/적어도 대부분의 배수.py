import math
from itertools import permutations
num = list(map(int,input().split()))
ans = int(1e9)
for x in permutations(num,3):
    x = list(x)
    ans = min(math.lcm(x[0],x[1],x[2]), ans)

print(ans)
    
    