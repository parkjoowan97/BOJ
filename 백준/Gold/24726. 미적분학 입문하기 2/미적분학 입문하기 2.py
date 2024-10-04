import sys
import copy
import math
input = sys.stdin.readline

x1,y1,x2,y2,x3,y3 = map(int,input().split())
pts = [[x1,y1],[x2,y2],[x3,y3]]

pts.sort(key = lambda x: x[0])
sort_x_pts = copy.deepcopy(pts)
#x좌표 기준으로 정렬

pts.sort(key = lambda x:x[1])
sort_y_pts = copy.deepcopy(pts)
#y좌표 기준으로 정렬

def partial_vol(pt1,pt2):
    x1,y1 = pt1[0], pt1[1]
    x2,y2 = pt2[0], pt2[1]

    axis_x_vol, axis_y_vol = 0,0
    if x1 == x2:
        #x축 좌표는 동일한 경우이므로, x축 기준으로 회전했을때는 0
        x = x1
        axis_y_vol = math.fabs(math.pi * (x ** 2) * (y2 - y1))
    elif y1 == y2:
        #y축 좌표는 동일한 경우이므로, y축 기준으로 회전했을때는 0
        y = y1
        axis_x_vol = math.fabs(math.pi * (y ** 2) * (x2 - x1))
    else:
        a = (y2 - y1) / (x2 - x1)
        b = (x2 * y1 - x1 * y2) / (x2 - x1)
        c = (x2 - x1) / (y2 - y1)
        d = (y2 * x1 - x2 * y1) / (y2 - y1)

        axis_x_vol = math.fabs((x2 ** 3 - x1 ** 3) * (a ** 2 / 3) + (x2 ** 2 - x1 ** 2) * (a * b) + (x2 - x1) * b ** 2) * math.pi
        axis_y_vol = math.fabs((y2 ** 3 - y1 ** 3) * (c ** 2 / 3) + (y2 ** 2 - y1 ** 2) * (c * d) + (y2 - y1) * d ** 2) * math.pi
    return axis_x_vol, axis_y_vol

answer_x = math.fabs(partial_vol(sort_x_pts[0], sort_x_pts[1])[0] + partial_vol(sort_x_pts[1], sort_x_pts[2])[0] - partial_vol(sort_x_pts[2], sort_x_pts[0])[0])
answer_y = math.fabs(partial_vol(sort_y_pts[0], sort_y_pts[1])[1] + partial_vol(sort_y_pts[1], sort_y_pts[2])[1] - partial_vol(sort_y_pts[2], sort_y_pts[0])[1])

print(answer_x, answer_y)