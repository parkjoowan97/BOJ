import sys
input = sys.stdin.readline

t = int(input())
for _ in range (0,t):
    pt = []
    for i in range (0,4):
        a = list(map(int,input().split()))
        pt.append(a)
    pt.sort(key = lambda x: (x[0], x[1]))
    if (pt[1][0] - pt[0][0]) ** 2 + (pt[1][1] - pt[0][1]) ** 2 == (pt[2][0] - pt[0][0]) ** 2 + (pt[2][1] - pt[0][1]) ** 2:
        if (pt[1][0] - pt[0][0]) * (pt[2][0] - pt[0][0]) + (pt[1][1] - pt[0][1]) * (pt[2][1] - pt[0][1]) == 0 and (pt[1][0] - pt[-1][0]) * (pt[2][0] - pt[-1][0]) + (pt[1][1] - pt[-1][1]) * (pt[2][1] - pt[-1][1]) == 0:
            print(1)
        else:
            print(0)
    else:
        print(0)