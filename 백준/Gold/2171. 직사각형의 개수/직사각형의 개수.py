import sys
from itertools import combinations
def input():
    return sys.stdin.readline().strip()

N = int(input())
set_pts = set()
pts = []

for _ in range (N):
    x, y = map(int,input().split())
    set_pts.add((x, y))
    pts.append([x, y])

answer = 0
for pt1, pt2 in combinations(pts, 2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    if (x1 != x2) and (y1 != y2) and (x1, y2) in set_pts and (x2, y1) in set_pts:
        answer += 1

print(answer // 2)