x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def between(a, b, c):
    return min(a, b) <= c <= max(a, b)

def det(a, b, c, d):
        return a * d - b * c
    
def direction(xa, ya, xb, yb, xc, yc):
        return det(xb - xa, yb - ya, xc - xa, yc - ya)
    
def intersecting(x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = direction(x3, y3, x4, y4, x1, y1)
    d2 = direction(x3, y3, x4, y4, x2, y2)
    d3 = direction(x1, y1, x2, y2, x3, y3)
    d4 = direction(x1, y1, x2, y2, x4, y4)
    if d1 * d2 < 0 and d3 * d4 < 0:
        return 1
    if d1 == 0 and between(x3, x4, x1) and between(y3, y4, y1):
        return 1
    if d2 == 0 and between(x3, x4, x2) and between(y3, y4, y2):
        return 1
    if d3 == 0 and between(x1, x2, x3) and between(y1, y2, y3):
        return 1
    if d4 == 0 and between(x1, x2, x4) and between(y1, y2, y4):
        return 1
    return 0

print(intersecting(x1, y1, x2, y2, x3, y3, x4, y4))