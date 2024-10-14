from collections import deque
n,m = map(int,input().split())
mapp = []
deq = deque()
checked = [[False for _ in range (0,m)] for _ in range (0,n)]
for i in range (0,n):
    a = input()
    mapp.append(a)
    if len(deq) == 0:
        for j in range (0,m):
            if a[j] == "I":
                deq.appendleft([i,j])
                checked[i][j] = True

dx,dy = [1,-1,0,0], [0,0,1,-1]
cnt = 0
while deq:
    z = deq.popleft()
    x,y = z[0], z[1]
    for k in range (0,4):
        xx, yy = x + dx[k], y + dy[k]
        if 0 <= xx < n and 0 <= yy < m and checked[xx][yy] == False:
            checked[xx][yy] = True
            if mapp[xx][yy] == "O" or mapp[xx][yy] == "P": 
                if mapp[xx][yy] == "P":
                    cnt += 1            
                deq.append([xx,yy])

if cnt == 0:
    print("TT")
else:
    print(cnt)