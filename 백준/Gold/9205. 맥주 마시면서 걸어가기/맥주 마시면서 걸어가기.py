import sys
from collections import deque

def bfs(home, conbini, penta, visited):
    deq = deque()
    deq.append((home[0],home[1]))
    while deq:
        x,y = deq.popleft()
        if abs(x - penta[0]) + abs(y - penta[1]) <= 1000:
            print('happy')
            return
        for i in range (0, len(conbini)):
            if not visited[i]:
                new_x,new_y = conbini[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    visited[i] = True
                    deq.append((new_x,new_y))
    print('sad')
    return

t = int(input())
for _ in range (0,t):
    n = int(input()) #편의점 갯수
    home = list(map(int,input().split()))
    conbini = []
    for i in range (0,n):
        con = list(map(int,input().split()))
        conbini.append(con)
    penta = list(map(int,input().split()))
    visited = [False for _ in range (0, n+1)]
    bfs(home, conbini, penta, visited)
    