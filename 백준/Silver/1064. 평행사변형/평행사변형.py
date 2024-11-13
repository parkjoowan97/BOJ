import math
x1,y1,x2,y2,x3,y3 = map(int,input().split())

def cal(x1,y1,x2,y2,x3,y3):
    if (y2 - y1) * (x3 - x2) == (x2 - x1) * (y3 - y2):
        return -1
    length = []
    #case 1
    around = 2 * (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2))
    length.append(around)
    #case 2
    around = 2 * (math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2) + math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2))
    length.append(around)
    #case 3
    around = 2 * (math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2) + math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    length.append(around)
    return max(length) - min(length)

print(cal(x1,y1,x2,y2,x3,y3))
