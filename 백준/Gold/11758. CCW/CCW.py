import sys
input = sys.stdin.readline
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
vec1,vec2 = [x2-x1, y2-y1],[x3-x2, y3-y2]
def ccw(vec1,vec2):
    answer = vec1[0] * vec2[1] - vec1[1] * vec2[0]
    if answer > 0:
        return 1
    elif answer == 0:
        return 0
    else:
        return -1
answer = ccw(vec1,vec2)
print(answer)